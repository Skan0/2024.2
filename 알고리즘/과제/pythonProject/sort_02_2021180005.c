#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
  const char *name;
  int x, y;
} City;

City cities[] = {
    {"Clean", 1336, 536}, {"Prosy", 977, 860},  {"Rabbi", 6, 758},    {"Addle", 222, 261},
    {"Smell", 1494, 836}, {"Quite", 905, 345},  {"Lives", 72, 714},   {"Cross", 23, 680},
    {"Synth", 1529, 785}, {"Tweak", 1046, 426}, {"Medic", 1485, 514}, {"Glade", 660, 476},
    {"Breve", 1586, 448}, {"Hotel", 1269, 576}, {"Toing", 398, 561},  {"Scorn", 617, 373},
    {"Tweet", 1253, 403}, {"Zilch", 1289, 29},  {"React", 296, 659},  {"Fiche", 787, 278},
};

void City_print(City *c)
{
  printf("%s(%d,%d)", c->name, c->x, c->y);
}
void City_printAll(City *p, int count)
{
  for (int i = 0; i < count; i++, p++) {
    City_print(p);
    putchar(' ');
  }
  putchar('\n');
}
void City_printAll_ptr(City **pp, int count)
{
  for (int i = 0; i < count; i++) {
    City_print(pp[i]);
    putchar(' ');
  }
  putchar('\n');
}
int static City_compare_name_asc(const void*a, const void*b){
    City*c1 = (City*)a;
    City*c2 = (City*)b;
    printf("%s vs %s\n",c1->name,c2->name);
    return strcmp(c1->name, c2->name);
}

int static City_compare_y_asc(const void*a, const void*b){
    City*c1 = (City*)a;
    City*c2 = (City*)b;
    
    return c1->y-c2->y;
}
int static City_ptr_compare_x_desc(const void*a, const void*b){
    City *c1 = *(City **)a;
    City *c2 = *(City **)b;
    
    return c2->x - c1->x;
}
int main(void) 
{
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));
  
  // sort here by name
  qsort(cities,sizeof(cities)/sizeof(cities[0]),sizeof(cities[0]),City_compare_name_asc);
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));
  
  // sort here by y coordinate
  qsort(cities,sizeof(cities)/sizeof(cities[0]),sizeof(cities[0]),City_compare_y_asc);
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));
  
  int city_count = sizeof(cities)/sizeof(cities[0]);
  City ** city_pointers = (City**)malloc(sizeof(City*)*city_count);
  for(int i =0;i<city_count;i++){
      city_pointers[i] = (City*)malloc(sizeof(City));
      *city_pointers[i] = cities[i];
  }
  
  City_printAll_ptr(city_pointers,city_count);
  
  qsort(city_pointers, city_count, sizeof(City*), City_ptr_compare_x_desc);
  City_printAll_ptr(city_pointers, city_count);
  
  for(int i =0;i<city_count;i++){
      free(city_pointers[i]);
  }
  free(city_pointers);
  
  return 0;
}