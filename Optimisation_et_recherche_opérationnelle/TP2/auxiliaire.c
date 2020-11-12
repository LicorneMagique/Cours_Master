

#define MAX_LINE_LENGTH 1000



///////////////////////////////////////////////////////////
////////////////   UTILITY FUNCTIONS   ////////////////////
///////////////////////////////////////////////////////////


//////////////////////////////////////////////////////
// SORTIR DU PROGRAMME AVEC UNE ERREUR
// precondition: s est initialise
// postcondition: ecrit la chaine de caractere pointee par s sur la sortie d'erreur standard et sort du programme avec le code d'erreur -1
void report_error(char *s){
  fprintf(stderr,"%s\n",s);
  exit(-1);
}




///////////////////////////////////////////////////////////
/////////////////   ADJACENCY LISTS   /////////////////////
///////////////////////////////////////////////////////////


typedef struct cell{
  int node;
  struct cell* suiv;
  struct cell* prec;
} cell;


typedef struct nodl{
  cell* prem;
  cell* dern;
} nodl;


//////////////////////////////////////////////////////
// INSERER UNE CELLULE APRES UNE AUTRE DANS UNE LISTE
// precondition: l est non null et pointe sur une liste non vide, p (non null) pointe sur une cellule de la liste pointee par l
// postcondition: une nouvelle cellule contenant la valeur u est inseree dans la liste pointee par l apres la cellule pointee par p 
void inserer_apres (int u, nodl* l, cell* p) {
	
	cell* q;
	if( (q=(cell *)malloc(sizeof(cell))) == NULL )
    report_error("graph_from_file: malloc() error 1");
	q->node=u;
  
	if (p->suiv==NULL) l->dern=q;
	else p->suiv->prec=q;  
    
	q->suiv=p->suiv;
	q->prec=p;
	p->suiv=q;
	
}

//////////////////////////////////////////////////////
// INSERER UNE CELLULE EN TETE D'UNE LISTE
// precondition: l est non null et *l est initialise
// postcondition: une nouvelle cellule contenant la valeur u est inseree en tete de la liste pointee par l 
void inserer_en_tete (int u, nodl* l) {

	cell* q;
	if( (q=(cell *)malloc(sizeof(cell))) == NULL )
    report_error("graph_from_file: malloc() error 1");
	q->node=u;
  
	if (l->dern==NULL) l->dern=q;
  
	q->suiv=l->prem;
	if (l->prem!=NULL) l->prem->prec=q;
	q->prec=NULL;
	l->prem=q;

}


//////////////////////////////////////////////////////
// INSERER UNE CELLULE EN QUEUE D'UNE LISTE
// precondition: l est non null et *l est initialise
// postcondition: une nouvelle cellule contenant la valeur u est inseree en queue de la liste pointee par l 
void inserer_en_queue (int u, nodl* l) {
	
	if (l->dern!=NULL) inserer_apres (u, l, l->dern);
	else inserer_en_tete (u, l);
}


//////////////////////////////////////////////////////
// SUPPRIMER UNE CELLULE D'UNE LISTE
// precondition: l est non null et pointe sur une liste non vide, p (non null) pointe sur une cellule de la liste pointee par l
// postcondition: la cellule pointee par p est retiree de la liste pointee par l et detruite 
void supprimer (cell* p, nodl* l){

	if (p->prec==NULL) {
		l->prem=p->suiv;
	}
	else {
		p->prec->suiv=p->suiv;
	}
	if (p->suiv==NULL) {
		l->dern=p->prec;
	}
	else {
		p->suiv->prec=p->prec;
	}

	free(p);

}


//////////////////////////////////////////////////////
// VIDER UNE LISTE
// precondition: aucune
// postcondition: supprime toutes les cellules de la liste pointee par l en liberant l'espace qu'elles prennent, la liste pointee par l est laissee vide
void vider(nodl* l) {
	if (l!=NULL){
		while (l->prem!=NULL) {
			supprimer(l->prem,l);
		}
	}	
}


//////////////////////////////////////////////////////
// VIDER ET LIBERER UNE LISTE
// precondition: aucune
// postcondition: libere l'espace memoire pris par la liste pointee par l et toutes ses cellules 
void free_nodl(nodl* l) {
	if (l!=NULL){
		vider(l);
		free(l);
	}	
}


//////////////////////////////////////////////////////
// COPIER LE CONTENU D'UNE LISTE A LA FIN D'UNE AUTRE
// precondition: l_dest et l_sour sont non null et *l_dest et *l_sour sont initialisees
// postcondition: les cellules de l_sour sont copiees et ajoutees a la fin de l_dest, dans le meme ordre
void copy_append (nodl* l_dest, nodl* l_sour) {
	cell* p=l_sour->prem;
	while (p!=NULL){
		inserer_en_queue(p->node,l_dest);
		p=p->suiv;
	}
}






///////////////////////////////////////////////////////////
////////////   GRAPH MANAGEMENT FUNCTIONS   ///////////////
///////////////////////////////////////////////////////////


typedef struct graph{
  int n;
  int m;
  nodl** links;
  int *degrees;
} graph;


//////////////////////////////////////////////////////
// CHARGER UN GRAPHE A PARTIR D'UN FLUX
// precondition: f est initialise et contient un graphe au format suivant: la premiere ligne contient un entier n qui est le nombre de sommets du graphe, chaque ligne suivante contient une arete du graphe representee par deux entiers compris entre 0 et n-1 (les identifiants des sommets) separes par un espace
// postcondition: initialise une structure graph, l'affecte du graphe lu sur le flux f et retourne un pointeur sur la structure graph ainsi construite
graph* graph_from_file(FILE *f){
  char line[MAX_LINE_LENGTH];
  int i, u, v;
  graph *g;

  if( (g=(graph *)malloc(sizeof(graph))) == NULL )
    report_error("graph_from_file: malloc() error 1");
  
  /* read n */
  if( fgets(line,MAX_LINE_LENGTH,f) == NULL )
    report_error("graph_from_file: read error (fgets) 1");
  if( sscanf(line, "%d\n", &(g->n)) != 1 )
    report_error("graph_from_file: read error (sscanf) 2");
  
  /* create space for links and degrees*/
  if (g->n==0){
    g->links = NULL; g->degrees = NULL;
  }
  else {
  
  	if( (g->degrees=(int*)malloc(g->n*sizeof(int))) == NULL )
      report_error("graph_from_file: malloc() error 3");
    for(i=0;i<g->n;i++){
    	g->degrees[i]=0;
    }
      
    if( (g->links=(nodl**)malloc(g->n*sizeof(nodl*))) == NULL )
      report_error("graph_from_file: malloc() error 3");
    for(i=0;i<g->n;i++){
    	if( (g->links[i]=(nodl*)malloc(sizeof(nodl))) == NULL )
      	report_error("graph_from_file: malloc() error 3");
	    g->links[i]->prem=NULL;
	    g->links[i]->dern=NULL;
    }
    
  }

  /* read the links */
  while (fgets(line,MAX_LINE_LENGTH,f) != NULL ){
    if( sscanf(line, "%d %d\n", &u, &v) != 2 ){
      fprintf(stderr,"Attempt to scan link #%d failed. Line read:%s\n", i, line);
      report_error("graph_from_file; read error (sscanf) 3");
    }
    if ( (u>=g->n) || (v>=g->n) || (u<0) || (v<0) ) {
      fprintf(stderr,"Line just read: %s",line);
      report_error("graph_from_file: bad node number");
    }
    
    inserer_en_queue(v, g->links[u]);
    inserer_en_queue(u, g->links[v]);
    g->degrees[u]++;
    g->degrees[v]++;
  }
  
  /* compute the number of links */
  g->m=0;
  for(i=0;i<g->n;i++)
    g->m += g->degrees[i];
  g->m /= 2;
  
  return g;
}


//////////////////////////////////////////////////////
// ECRIRE UN GRAPHE DANS UN FLUX
// precondition: f et g sont initialises
// postcondition: le graphe pointe par g est ecrit sur le flux f dans le format suivant: la premiere ligne contient un entier qui est le nombre de sommets du graphe, chaque ligne suivante contient une arete du graphe representee par deux entiers (les identifiants des sommets) separes par un espace
void write_graph(FILE *f, graph* g){

	int u;
	cell* p;

	fprintf(f,"%d\n",g->n);
	for (u=0;u<g->n;u++) {
		p=g->links[u]->prem;
  	while (p!=NULL) {
			if (p->node<u) fprintf(f,"%d %d\n",u,p->node);
			p=p->suiv;
		}
	}
	fflush(f);	
}


//////////////////////////////////////////////////////
// LIBERER UN GRAPHE
// precondition: aucune
// postcondition: libere l'espace memoire pris par le graphe, son tableau degrees et son tableau links
void free_graph(graph *g){
	int i;
  if (g!=NULL) {
    if (g->links!=NULL) {
    	for(i=0;i<g->n;i++) {
    		free_nodl(g->links[i]);
    	}
      free(g->links);
    }
    if (g->degrees!=NULL)
      free(g->degrees);
    free(g);
  }
}



///////////////////////////////////////////////////////////
//////////   DISPLAY FUNCTIONS FOR DEBUGGING   ////////////
///////////////////////////////////////////////////////////



void vwrite_degrees(graph* g, FILE *f){
	int i;
	for (i=0;i<g->n;i++){
		fprintf(f,"d(%d)=%d; ", i,g->degrees[i]);
	}
	fprintf(f,"\n");
	fflush(f);
}


void vwrite_cell(cell* c, FILE *f){
	fprintf(f,"@@@@ : %lx\n", (long unsigned int) c);
	fprintf(f,"node : %d\n", c->node);
	fprintf(f,"prec : %lx\n", (long unsigned int) c->prec);
	fprintf(f,"suiv : %lx\n", (long unsigned int) c->suiv);
	fflush(f);
}


void vwrite_graph(graph* g, FILE *f){

	int u;
	cell* p;

	fprintf(f,"n: %d\n",g->n);
	fprintf(f,"m: %d\n",g->m);
	
	fprintf(f,"*** Degres ***  ");
	fflush(f);
	vwrite_degrees(g,f);
	fprintf(f,"\n");
	
	
	for (u=0;u<g->n;u++) {
		fprintf(f,"***************\n");
		fprintf(f,"Liste de : %d\n",u);
		fprintf(f,"***************\n");
		fflush(f);
		if (g->links[u]==NULL){
			fprintf(f,"FUSIONNE\n");
		}
		else{ 
			p=g->links[u]->prem;
  		while (p!=NULL) {
				vwrite_cell(p,f);
				fprintf(f,"\n");
				fflush(f);
				p=p->suiv;
			}
		}
		fprintf(f,"\n");
	}
	
	fflush(f);
	
}




///////////////////////////////////////////////////////////
////////////////   RANDOM FUNCTIONS   /////////////////////
///////////////////////////////////////////////////////////


/////////////////////////////////////
// INITIALISATION OF rand()
// with 2 inputs : n2 sensitive to program execution, n1 sensitive to moment of call in the execution

void init_random() {
  int n1, n2;
  struct timeval aux;
  gettimeofday(&aux,NULL);
  
  n1=(((int) clock())%100);
  n2=((int) aux.tv_usec)%1000;
  
  srand( (((((n2%10)*10+(n1%10))*10+(n2%10)%10)*10+(n1/10))*10+(n2/100))*10000+n1*100+n2 );
}



/////////////////////////////////////
// A RANDOM INTEGER BETWEEN 0 AND a
// an improved version, supposed to be as much uniform as rand() of C

int rand_imp(int a){
  int pas, limit, tir;
  
  if (a>RAND_MAX) report_error("Function rand_imp asks for a random integer possibly greater than RAND_MAX.\n");

  else if (a==RAND_MAX) {
    tir=rand();
    pas=1;
  }
  
  else if (a<RAND_MAX) {
    pas=RAND_MAX / (a+1);
    if (RAND_MAX % (a+1) == a) {
      pas++;
      limit=RAND_MAX;
    }
    else limit = (a+1) * pas - 1;

    tir=rand();
    while (tir>limit) {
    tir=rand();
    }
  }
  
  return tir/pas;
}



/////////////////////////////////////
// A RANDOM UNSIGNED INT BETWEEN 0 AND a
// an improved version, supposed to be as much uniform as rand() of C
unsigned int rand_imp_u(unsigned int a){
  unsigned int quotient, remain;
  unsigned int rand_remain, rand_quotient;
  unsigned int result;
  unsigned int power;
  unsigned int half_uint_max;

  half_uint_max=UINT_MAX/2 +1;
  while (UINT_MAX/half_uint_max < half_uint_max) {
    half_uint_max /=2;
  }
  half_uint_max *= 2;

  quotient= a / half_uint_max;
  remain= a % half_uint_max;

  if (quotient>0) {

    power = 1;
    while (power <= quotient) {
      power *= 2;
    }

    rand_quotient= (unsigned int) rand_imp(((int) power)-1);
    rand_remain= (unsigned int) rand_imp(((int) half_uint_max)-1);
    result = rand_quotient * half_uint_max + rand_remain;

    while (result > a) {
      rand_quotient= (unsigned int) rand_imp(((int) power)-1);
      rand_remain= (unsigned int) rand_imp(((int) half_uint_max)-1);
      result = rand_quotient * half_uint_max + rand_remain;
    }
  }
  else {
    result= (unsigned int) rand_imp((int) remain);
  }

  return result;
}



/////////////////////////////////////
// A RANDOM UNSIGNED LONG BETWEEN 0 AND a
// an improved version, supposed to be as much uniform as rand() of C

unsigned long rand_imp_ul(unsigned long a){
  unsigned long quotient, remain;
  unsigned long rand_remain, rand_quotient;
  unsigned long result;
  unsigned long power;

  quotient= a / (1 + (unsigned long) UINT_MAX);
  remain= a % (1 + (unsigned long) UINT_MAX);

  if (quotient>0) {

    power = 1;
    while (power <= quotient) {
      power *= 2;
    }

    rand_quotient= (unsigned long) rand_imp_u(((unsigned int) power) -1);
    rand_remain= (unsigned long) rand_imp_u(UINT_MAX);
    result = rand_quotient * (1+ (unsigned long) UINT_MAX) + rand_remain;

    while (result > a) {
      rand_quotient= (unsigned long) rand_imp_u(((unsigned int) power) - 1);
      rand_remain= (unsigned long) rand_imp_u(UINT_MAX);
      result = rand_quotient * (1+ (unsigned long) UINT_MAX) + rand_remain;
    }
  }
  else {
    result= (unsigned long) rand_imp_u((unsigned int) remain);
  }
  
  return result;
}





