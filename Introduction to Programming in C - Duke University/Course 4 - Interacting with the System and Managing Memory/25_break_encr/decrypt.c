#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <limits.h>

int get_max_index(int * arr, unsigned size) {  
  int max = INT_MIN;  
  int max_index = 0;
  
  for (int i = 0; i < size; i++) {    
    if (arr[i] > max) {      
      max = arr[i];      
      max_index = i;      
    }    
  }  
  return max_index;  
}


int get_key(int guess) {  
  int key = 0;
  
  if (guess >= 4 ) {    
    key = guess - 4;    
  } else {    
    key = 26 - (guess + 4);    
  }  
  return key;  
}

void decrypt(FILE * f) {  
  int c;  
  int crypt[26] = {0};
  
  while( (c = fgetc(f)) != EOF) {    
    if (isalpha(c)) {      
      c = tolower(c);      
      c -= 'a';      
      crypt[c] += 1;      
    }    
  }
  
  int guess = get_max_index(crypt, 26);  
  int key = get_key(guess);  
  printf("%d\n", key);  
}

int main(int argc, char ** argv) {  
  if (argc !=2) {    
    fprintf(stderr, "Usage: decrypt inputFileName\n");    
    return EXIT_FAILURE;    
  }
   
  FILE * f = fopen(argv[1], "r");  
  if (f == NULL) {    
    perror("Could not open file.");    
    return EXIT_FAILURE;    
  } 
  
  decrypt(f);
  
  if (fclose(f) != 0) {    
    perror("Failed to close the input file!");    
    return EXIT_FAILURE;    
  }  
  return EXIT_SUCCESS;  
}
