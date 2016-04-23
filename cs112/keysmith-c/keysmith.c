/*/
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
/*/


#define __AUTHOR__ "dmtucker@ucsc.edu"
#define OPTS "[-dv]"
#define ARGS "[degree]"

#include <curl/curl.h> // CURLOPT_URL, CURLOPT_WRITEFUNCTION, typedef CURL, typedef CURLcode, curl_easy_cleanup(), curl_easy_init(), curl_easy_perform(), curl_easy_setopt(), curl_easy_strerror()
#include   <stdbool.h> // typedef bool, false, true
#include     <stdio.h> // NULL, typedef FILE, fclose(), feof(), fgets(), fopen(), fprintf(), perror(), printf(), putchar(), puts(), rewind(), setbuf(), snprintf()
#include    <stdlib.h> // EXIT_FAILURE, EXIT_SUCCESS, typedef size_t, atoi()
#include    <string.h> // strlen(), strncat(), strncmp(), strncpy(), strtok()
#include      <time.h> // typedef time_t, time()
#include    <unistd.h> // optind, optopt, getopt()


/* constants */
static const int          DEFAULT_DEGREE = 3;
static const char * const DEFAULT_WORDS  = "word.list";
static const char * const VERSION        = "0.0";


/* globals */
bool DETAILS = false;
bool VERBOSE = false;


/* RANDOM.ORG */
char * nonces;

size_t handler ( char * ptr , size_t size , size_t nmemb , void * userdata ) {
    nonces = ptr;
    return size * nmemb;
}


//* keysmith *//
int main ( int argc , char * argv[] ) {
    
    /* environment */
    setbuf(stdout,NULL);
    
    /* initialize */
    if (argc > 4) return (fprintf(stderr,"usage: %s %s %s\n",argv[0],OPTS,ARGS) < 0) ? EXIT_FAILURE : EXIT_SUCCESS;
    extern int optind;
    while (true) {
        extern int optopt;
        switch (getopt(argc,argv,"dhvV")) {
            case -1: break;
            default: return EXIT_FAILURE;
            case 'h': (void) puts(argv[0]);
                (void) printf("\
  -d  Print key details\n\
  -h  Show help\n\
  -v  Enable verbose messages\n\
  -V  Print version\n\
");
                return EXIT_SUCCESS;
                
            case 'd': DETAILS = true; continue;
            case 'v': VERBOSE = true; continue;
            case 'V': (void) printf("%s\n",VERSION);
                return EXIT_SUCCESS;
        }
        break;
    }
    const int degree = (argc > optind) ? atoi(argv[optind]) : DEFAULT_DEGREE;
    
    
    /* words */
    if (VERBOSE) (void) printf("counting words in %s...",DEFAULT_WORDS);
    size_t list = 0;
    FILE * words = fopen(DEFAULT_WORDS,"r");
    if (words == NULL) {
        perror("unable to open the word list");
        return EXIT_FAILURE;
    }
    while (feof(words) == 0) {
        char word[1024];
        if (fgets(word,1024,words) == NULL) break;
        if (word[0] != '\n') ++list;
    }
    rewind(words);
    if (VERBOSE) (void) printf("%zd\n",list);
    if (list < 2) (void) fprintf(stderr,"word list is too short\n");
    
    
    //* nonces *//
    else {
        
        /* build */
        if (VERBOSE) (void) printf("retrieving random numbers...");
        char url[128];
        (void) strncpy(url,"https://www.random.org/integers/?num=",37);
        (void) snprintf(&url[strlen(url)],22,"%d",degree);
        (void) strncat(url,"&min=0&max=",11);
        (void) snprintf(&url[strlen(url)],22,"%zd",list-1);
        (void) strncat(url,"&col=1&base=10&format=plain&rnd=new",35);
        url[127] = '\0';
        if (DETAILS) {
            if (VERBOSE) (void) printf("\n  ");
            (void) printf("%s\n",url);
        }
        
        /* request */
        CURL * const curl = curl_easy_init();
        if (curl == NULL)  fprintf(stderr,"curl error\n");
        else {
            CURLcode status;
            if ((status = curl_easy_setopt(curl,CURLOPT_URL,url))               != CURLE_OK
            ||  (status = curl_easy_setopt(curl,CURLOPT_WRITEFUNCTION,handler)) != CURLE_OK
            ||  (status = curl_easy_perform(curl))                              != CURLE_OK) 
                fprintf(stderr,"curl error: %s\n",curl_easy_strerror(status));
            curl_easy_cleanup(curl);
        }
        if (nonces != NULL && strncmp(nonces,"Error:",6) == 0) {
            (void) fprintf(stderr,"%s\n",nonces);
            return EXIT_FAILURE;
        }
        if (VERBOSE) (void) puts("done");
        
        //*//
    }
    
    
    //* key *//
    if (nonces != NULL) {
        
        //* generate *//
        if (VERBOSE) (void) printf("generating a key...");
        if (VERBOSE && DETAILS) (void) putchar('\n');
        char key[1024];
        key[0] = '\0';
        bool error = false;
        char * nonce = strtok(nonces,"\n");
        for (int i = 0; i < degree ;++i) {
            if (nonce == NULL) {
                error = true;
                if (VERBOSE) (void) fprintf(stderr,"  ");
                (void) fprintf(stderr,"nonce famine\n");
                break;
            }
            
            /* loookup */
            char word[1024];
            for (int index = atoi(nonce); index >= 0 ;--index) {
                if (fgets(word,1024,words) == NULL) break;
                if (word[0] == '\n' || word[0] == '\0') ++index;
            }
            if (DETAILS) {
                if (VERBOSE) (void) printf("  ");
                (void) printf("%d => %s",atoi(nonce),word);
            }
            
            /* append */
            strncat(key,word,strlen(word)-1);
            
            //*//
            rewind(words);
            nonce = strtok(NULL,"\n");
        }
        
        
        //* deliver *//
        if (!error) {
            if (VERBOSE && DETAILS) (void) puts("done");
            
            /* print */
            if (DETAILS) {
                for (int i = strlen(key); i > 0 ;--i) (void) putchar('-');
                putchar('\n');
            }
            (void) printf("%s\n",key);
            if (DETAILS) {
                for (int i = strlen(key); i > 0 ;--i) (void) putchar('-');
                putchar('\n');
                (void) printf("%zd characters\n",strlen(key));
            }
            
            //*//
        }
        
        
        //*//
    }
    
    
    //*//
    if (fclose(words) != 0) perror("unable to close the word list");
    return EXIT_SUCCESS;
}
