
#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
//#include <unistd.h>

#include "auxiliaire.c"
#include "fonctions-algo.c"

/******************/
/* Default values */
/******************/

/********************/
/* Output functions */
/********************/

// print help
void usage(char *c) {
  fprintf(stderr, "Usage: %s -h\n", c);
  fprintf(stderr, "  -h: print current help.\n");
  fprintf(stderr, "  -i \"inputname\": input file containing the graph (default value is stdin).\n");
  fprintf(stderr, "  -o \"outputname\": output results in a file named \"outputname\" (default value is stdout).\n");
  exit(-1);
}

/**************************************************************/
/**************************************************************/
/**************************************************************/
/***************************        ***************************/
/***************************  MAIN  ***************************/
/***************************        ***************************/
/**************************************************************/
/**************************************************************/
/**************************************************************/

int main(int argc, char **argv) {

  ///////////////////////////////////////////////////////////
  //////////   DECLARATIONS AND DEFAULT VALUES   ////////////
  ///////////////////////////////////////////////////////////

  FILE* fin = NULL;
  FILE* fout = NULL;

  int i;

  graph* g;

  ///////////////////////////////////////////////////////////
  ////////////////   PARSE COMMAND LINE   ///////////////////
  ///////////////////////////////////////////////////////////

  // default values
  char name_in[100] = "";
  char name_out[100] = "";
  int input_file_given = 0;
  int output_file_given = 0;

  // user's values

  for (i = 1; i < argc; i++) {
    if ((strcmp(argv[i], "-h") == 0) || (strcmp(argv[i], "--help") == 0)) {
      usage(argv[0]);
    } else if ((strcmp(argv[i], "-i") == 0) || (strcmp(argv[i], "--input") == 0)) {
      if (i == argc - 1) {
        usage(argv[0]);
      }
      input_file_given = 1;
      strcpy(name_in,argv[++i]);
    } else if ((strcmp(argv[i], "-o") == 0) || (strcmp(argv[i], "--output") == 0)) {
      if (i == argc - 1) {
        usage(argv[0]);
      }
      output_file_given = 1;
      strcpy(name_out,argv[++i]);
    } else usage(argv[0]);
  }

  ///////////////////////////////////////////////////////////
  ///////////////////   OPEN FILES   ////////////////////////
  ///////////////////////////////////////////////////////////

  if (input_file_given == 0) {
    fin = stdin;
  } else {
    if ((fin = fopen(name_in, "r")) == NULL) {
      report_error("name_in -- fopen: error");
    }
  }

  if (output_file_given == 0) {
    fout = stdout;
  } else {
    if ((fout = fopen(name_out, "w")) == NULL) {
      report_error("name_out -- fopen: error");
    }
  }

  ///////////////////////////////////////////////////////////
  /////////   PRINT MAX VALUES ON THE MACHINE   /////////////
  ///////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////
  /////////////////   LOADING GRAPH   ///////////////////////
  ///////////////////////////////////////////////////////////

  fprintf(stderr, "Begin computation.\n");

  g = graph_from_file(fin);
  fprintf(stderr, "Sommets : %d\nArêtes : %d\n", g->n, g->m);
  fflush(stderr);

  ///////////////////////////////////////////////////////////
  //////////////////   DATA STRUCTURE   /////////////////////
  ///////////////////////////////////////////////////////////

  // un tableau de taille n qui a chaque sommet associe l’identifiant de son groupe et
  // — un tableau de taille n qui a chaque identifiant de groupe associe la liste des sommets
  // qu’il contient et
  // — un tableau de taille n qui a chaque identifiant de groupe associe le nombre de
  // sommets dans le groupe.

  ///////////////////////////////////////////////////////////
  /////////////////   COMPUTE MIN CUT   /////////////////////
  ///////////////////////////////////////////////////////////

  fprintf(stderr, "Begin computation.\n");
  fflush(stderr);

  ///////////////////////////////////////////////////////////
  //////////////////   OUTPUT RESULTS   /////////////////////
  ///////////////////////////////////////////////////////////

  // fprintf(stderr,"Outputing results.\n");
  // fflush(stderr);
  // write_graph(fout, g);

  ///////////////////////////////////////////////////////////
  ////////////   CLOSE FILES AND FREE MEMORY  ///////////////
  ///////////////////////////////////////////////////////////

  if (fin != NULL) {
    fclose(fin);
  }
  fprintf(stderr, "Input file closed.\n");
  fflush(stderr);

  if (fout != NULL) {
    fclose(fout);
  }
  fprintf(stderr, "Output file closed.\n");
  fflush(stderr);

  free_graph(g);

  return 0;
}

/**************************************************************/
/**************************************************************/
/*************************            *************************/
/*************************  FIN MAIN  *************************/
/*************************            *************************/
/**************************************************************/
/**************************************************************/
