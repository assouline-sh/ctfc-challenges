#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

void init() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
  init();

  
  printf("Welcome to my calculator!\n\n");
  system("/bin/cat art.txt");
  printf("\nProvide two integers between 0 and %d, inclusive\n\n", INT_MAX);

  int a;
  printf("Enter the first positive integer: ");
  if(scanf("%d", &a) != 1 || a <= 0) {
    printf("Invalid input. Exiting.\n");
    return 1;
  }

  int b;
  printf("Enter the second positive integer: ");
  if(scanf("%d", &b) != 1 || b <= 0) {
    printf("Invalid input. Exiting.\n");
    return 1;
  }

  int sum = a + b;
  printf("\nThe sum is %u\n\n", sum);

  // Check if the sum equals -1337 and give the flag if it does
  if (sum == -1337) {
    printf("Bonus! Your sum equals the special number! Here's your flag:\n");
    int ret = system("/bin/cat flag.txt");
  } else {
    printf("No flag for you! Exiting.");
  }
  printf("\n");
  
  return 0;
}