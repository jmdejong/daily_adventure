
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <errno.h>

#include "paths.h"

void printUsage(char *process){
    printf("Usage:\n  %s printinput\n  %s setinput\n  %s printinfo\nprintinput and printinfo will print to stdout.\nsetinput will read from stdin.\n", process, process, process);
}


void printfile(char *filename){
    FILE *f = fopen(filename, "r");
    if (f == NULL){
        fprintf(stderr, "Unable open %s\n", filename);
        return;
    }
    // print all output from a file to stdout
    int c;
    while ((c = fgetc(f), c != EOF)){
        fputc(c, stdout);
    }
    pclose(f);
}


void writefile(char *filename){
    FILE *f = fopen(filename, "w");
    if (f == NULL){
        fprintf(stderr, "Unable open %s\n", filename);
        return;
    }
    // write all input from stdin to a file
    int c;
    while ((c = fgetc(stdin), c != EOF)){
        fputc(c, f);
    }
    pclose(f);
    chmod(filename, 0600);
}




void printInput(char *username){
    char fname[100];
    sprintf(fname, inputfname, username);
    printfile(fname);
}

void setInput(char *username){
    char fname[100];
    sprintf(fname, inputfname, username);
    writefile(fname);
}


void printInfo(char* username){
    char fname[100];
    sprintf(fname, infofname, username);
    printfile(fname);
}

int main(int argc, char *argv[]){
    
    if (argc != 2){
        printUsage(argv[0]);
        return 0;
    }
    char username[80];
    getlogin_r(username, 80);
    char *command = argv[1];
    if (!strcmp(command, "printinput")){
        printInput(username);
    } else if (!strcmp(command, "setinput")){
        setInput(username);
    } else if (!strcmp(command, "printinfo")){
        printInfo(username);
    } else {
        printUsage(argv[0]);
    }
    if (errno) {
        fprintf(stderr, "Error %d: ", errno);
        perror("");
    }
    return errno;
}
