
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
//#include "fonctions-algo.c"



/********************/
/* Output functions */
/********************/

// print help
void usage(char *c){
	fprintf(stderr,"Usage: %s -h\n",c);
	fprintf(stderr,"  -h: print current help.\n");
	fprintf(stderr,"  -l: list all maximum stable sets, with possible repetitions.\n");
	fprintf(stderr,"  -i \"inputname\": input file containing the graph (default value is stdin).\n");
	fprintf(stderr,"  -o \"outputname\": output results in a file named \"outputname\" (default value is stdout).\n");
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


int main(int argc, char **argv){


///////////////////////////////////////////////////////////
//////////   DECLARATIONS AND DEFAULT VALUES   ////////////
///////////////////////////////////////////////////////////
 
	FILE* fin=NULL;
	FILE* fout=NULL;

	graph * G=NULL;

	int i;





///////////////////////////////////////////////////////////
////////////////   PARSE COMMAND LINE   ///////////////////
///////////////////////////////////////////////////////////


	// default values
	char name_in[100]="";
	char name_out[100]="";
	bool input_file_given=false;
	bool output_file_given=false;
	bool liste=false;

	// user's values
  
	for (i=1; i<argc; i++) {
		if ((strcmp(argv[i],"-h")==0) || (strcmp(argv[i],"--help")==0) ) {
			usage(argv[0]);     
		}
		else if ((strcmp(argv[i],"-l")==0) || (strcmp(argv[i],"--liste")==0) ) {
			liste=true;
		}
		else if ((strcmp(argv[i],"-i")==0) || (strcmp(argv[i],"--input")==0) ) {
			if (i==argc-1)
				usage(argv[0]);
			input_file_given=true;
			strcpy(name_in,argv[++i]);
		}
		else if ((strcmp(argv[i],"-o")==0) || (strcmp(argv[i],"--output")==0) ) {
			if (i==argc-1)
				usage(argv[0]);
			output_file_given=true;
			strcpy(name_out,argv[++i]);
		}
		else usage(argv[0]);
	}




  
///////////////////////////////////////////////////////////
///////////////////   OPEN FILES   ////////////////////////
///////////////////////////////////////////////////////////

	if (!input_file_given) {
		fin=stdin;
	}
	else {
		if ( (fin=fopen(name_in,"r"))==NULL)
			report_error("name_in -- fopen: error");
	}


	if (!output_file_given) 
		fout=stdout;
	else {
		if ( (fout=fopen(name_out,"w"))==NULL)
			report_error("name_out -- fopen: error");
	}

  	

///////////////////////////////////////////////////////////
/////////////////   LOADING GRAPH   ///////////////////////
///////////////////////////////////////////////////////////

	fprintf(stderr,"Reading the graph...\n");
	G = graph_from_file(fin);

	fprintf(stderr,"%d vertices, %d edges in the graph\n",G->n,G->m);
	fflush(stderr);
  
	if (fin!=NULL) {
		fclose(fin);
		fin=NULL;
		fprintf(stderr,"Input file closed.\n");
		fflush(stderr);
	}

 

///////////////////////////////////////////////////////////
//////////////////   DATA STRUCTURE   /////////////////////
///////////////////////////////////////////////////////////

  
  
  
  
  


///////////////////////////////////////////////////////////
///////////////   COMPUTE MAX STABLE   ////////////////////
///////////////////////////////////////////////////////////

	fprintf(stderr,"Begin computation.\n");
	fflush(stderr);





///////////////////////////////////////////////////////////
//////////////////   OUTPUT RESULTS   /////////////////////
///////////////////////////////////////////////////////////

  fprintf(stderr,"Outputing results.\n");
  fflush(stderr);





///////////////////////////////////////////////////////////
////////////   CLOSE FILES AND FREE MEMORY  ///////////////
///////////////////////////////////////////////////////////
	
	if (fout!=NULL) {
		fclose(fout);
		fprintf(stderr,"Output file closed.\n");
		fflush(stderr);
	}

	free_graph(G);

  fprintf(stderr,"Memory freed.\n");
  fflush(stderr);


	return 0;
}

/**************************************************************/
/**************************************************************/
/*************************            *************************/
/*************************  FIN MAIN  *************************/
/*************************            *************************/
/**************************************************************/
/**************************************************************/


