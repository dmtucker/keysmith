{-
 This file is part of keysmith.
 
 keysmith is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 keysmith is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with keysmith. If not, see <http://www.gnu.org/licenses/>.
-}


module Main ( main , buildKey ) where

import Control.Monad -- when
import Data.Functor -- <$>
import Network.HTTP -- getRequest, getResponseBody, simpleHTTP
import System.Console.GetOpt -- getOpt, NoArg, OptDescr, Option, RequireOrder, usageInfo
import System.IO -- hPutStrLn, hSetBuffering, NoBuffering, putStrLn, stderr, stdout
import System.Environment -- getArgs, getProgName
import System.Exit -- exitFailure, exitSuccess
--import System.Random.Atmosphere


{- constants -}
defaultDegree = 3 :: Int
defaultWords  = "word.list" :: String
version       = "0.0" :: String


{- options -}
data Options   = Options { optVerbose :: Bool }
defaultOptions = Options { optVerbose = False }

options :: [ OptDescr (Options -> IO Options) ]
options =
    [ Option "h" ["help"]
        (NoArg (\_ -> do name <- getProgName
                         hPutStrLn stderr (usageInfo name options)
                         exitSuccess))
        "Show help"

    , Option "v" ["verbose"]
        (NoArg (\opt -> return opt { optVerbose = True }))
        "Enable verbose messages"

    , Option "V" ["version"]
        (NoArg (\_ -> do hPutStrLn stderr version
                         exitSuccess))
        "Print version"
    ]


buildKey :: [String] -> [Int] -> String
buildKey words [] = ""
buildKey words (nonce:nonces) = (words !! nonce) ++ buildKey words nonces


{- keysmith -}
main = do
    
    {- environment -}
    hSetBuffering stdout NoBuffering
    
    
    {- initialize -}
    args <- getArgs
    when (length args > 4) $ ("Usage: " ++) . (++ " [-hvV] [degree]") <$> getProgName >>= (hPutStrLn stderr) >> exitFailure
    let (actions, nonOptions, errors) = getOpt RequireOrder options args
    when (errors /= []) (hPutStr stderr (head errors) >> exitFailure)
    opts <- foldl (>>=) (return defaultOptions) actions
    let Options { optVerbose = verbose } = opts
    let degree = case nonOptions of
                     []     -> defaultDegree :: Int
                     (x:[]) -> read x :: Int
                     (x:xs) -> error "Too many arguments"
    
    
    {- words -}
    when verbose (putStr ("counting words in "++defaultWords++"..."))
    words <- fmap lines (readFile defaultWords)
    let list = length words
    when verbose (print list)
    when (list < 2) (hPutStrLn stderr "word list is too short" >> exitFailure)
    
    
    {- nonces -}
    when verbose (putStr ("retrieving random numbers..."))
    response <- simpleHTTP (getRequest ("https://www.random.org/integers/?num="++(show degree)++"&min=0&max="++(show (list-1))++"&col=1&base=10&format=plain&rnd=new"))
    nonces <- (fmap (map read . take degree . lines) (getResponseBody response))
    when verbose (putStrLn "done")
    when (length nonces /= degree) (hPutStrLn stderr "nonce famine" >> exitFailure)
    
    
    {- key -}
    when verbose (putStr ("generating a key..."))
    let key = buildKey words nonces
    putStrLn key
    
    
    --{-}--
    exitSuccess
