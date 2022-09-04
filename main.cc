/**
 * A simulation of a virus in a population
 * @file main.cc

 * @author William Crane-Morris
 * @date May 10, 2022
 * Style edits.
 */
#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <fstream>

#include "Person.h"

std::ofstream myfile("output.txt"); // just so it has global scope

const size_t INIT_NUM_INFECTED = 4; // how many people to infect at start
const size_t DAY_TO_HEAL = 5; // when Person has chance of healing
// const size_t RECIPROCAL_CHANCE_TO_HEAL = 10; // each day after day 5, a 1/10 chance to be healed
const size_t DAY_TO_DIE = 15; // time of infection where person dies
const size_t PERCENT_CHANCE_INFECT_HEALTHY = 5;
const size_t PERCENT_CHANCE_INFECT_RECOVERED = 3;


void print_per_vect(std::vector<Person> const populace)
{
   // std::cout << populace.size() << '\n' << '\n';
   for (Person individual : populace)
   {
      std::cout << individual.get_status_str() << individual.get_name() << '\n';
   }
}

/* prints and outputs a vector<size_t>
 * param vec the vector we are printing
 */
void print_size_t_vec(std::vector<size_t> const vec)
{
   for (size_t element : vec)
   {
      std::cout << element << ", ";
      myfile << element << ", ";
   }
   std::cout << '\n';
   myfile << '\n';
}

/* Initializes the population
 * Param populace the vector holding all the Persons
 * Param population how many people are in the simulation
 */
void fill_population(std::vector<Person> &populace, size_t const population)
{
   // populace.resize(population);  // redundant
   populace.clear();    // to get rid of no argument constructed Persons
   for (size_t index = 0; index < population; index++)
   {
      populace.push_back(Person(index));
   }
}

/* initializes the num infected of infected people
 * Param populace the vector holding all the Persons
 */
void infect_people(std::vector<Person> &populace)
{
   for (size_t index = 0; index < INIT_NUM_INFECTED; index++)
   {
      // std::cout << "bingus";
      populace[index].infect();
      // std::cout << populace[index].get_status_str() << '\n';
   }
}

/* returns as a std::vector<size_t> the current status of all the people in the population
 * Param populace the vector holding all the Persons
 */
std::vector<size_t> curr_aggregate_status(std::vector<Person> const populace)
{
   size_t healthy = 0;
   size_t infected = 0;
   size_t recovered = 0;
   size_t dead = 0;
   for (Person individual : populace)
   {
      if (individual.get_status_num() == 0)
      {
         healthy += 1;
      }
      else if (individual.get_status_num() == 1)
      {
         infected += 1;
      }
      else if (individual.get_status_num() == 2)
      {
         recovered += 1;
      }
      else
      {
         dead += 1;
      }
   }
   std::vector<size_t> output = {healthy, infected, recovered, dead};
   return output;
}

/* initializes the how many connections each person has
 * Param populace the vector holding all the Persons
 * param population # of people in populace
 * param upper_bound largest num of connections allowed
 */
void set_conn_nums(std::vector<Person> &populace, size_t const population, size_t upper_bound)
{
   for (size_t index = 0; index < population; index++)
   {
      size_t conns = ((upper_bound - 1) / (rand() % upper_bound + 1)) + 1;
      populace[index].set_max_connec(conns);
   }
}

/* returns vector of all the # of connections the infected people have
 * Param populace the vector holding all the Persons
 */
std::vector<size_t> close_contacts(std::vector<Person> const populace)
{
   std::vector<size_t> output;
   for (Person individual : populace)
   {
      if (individual.get_status_num() == 1)
      {
         output.emplace_back(individual.get_max_conns());
      }
   }
   return output;
}

/* randomly infects people who are health or recovered based on the # of close contacts
 * Param populace the vector holding all the Persons
 * param population # of Persons
 * param contacts vector of the # of connections of all the infected people
 */
void spread_disease(std::vector<Person> &populace, size_t const population, std::vector<size_t> contacts)
{
   size_t total = 0;
   for (size_t element : contacts)
   {
      total += element;
   }
   for (size_t counter = 0; counter < total; counter++)
   {
      size_t rand_index = rand() % population;
      if (populace[rand_index].get_status_num() == 0)
      {
         if (( rand() % 100) < int(PERCENT_CHANCE_INFECT_HEALTHY))
         {
            populace[rand_index].infect();
         }
      }
      else if (populace[rand_index].get_status_num() == 2)
      {
         if ((rand() % 100) < int(PERCENT_CHANCE_INFECT_RECOVERED))
         {
            populace[rand_index].infect();
         }
      }
   }
}

/* implements the number of time steps and puts all the actions together in order
 * Param populace the vector holding all the Persons
 */
void time_steps(std::vector<Person> &populace, size_t const population, size_t run_time)
{
   for (size_t time = 0; time < run_time; time++)
   {
      std::cout << time << ", ";
      myfile << time << ", ";
      print_size_t_vec(curr_aggregate_status(populace));
      for (size_t index = 0; index < population; index ++)
      {
         if (populace[index].get_status_num() == 1)
         {
            if (populace[index].get_time_infected() > DAY_TO_HEAL)
            {
               if (rand() % 10 < 1) // 10% change of healing
               {
                  populace[index].heal();
               }
            }
            if (populace[index].get_time_infected() > DAY_TO_DIE)
            {
               populace[index].kill();
            }
            populace[index].time_infected_plus();
         }
      }
      spread_disease(populace, population, close_contacts(populace));
   }
}


// controls flow of the program
int main()
{
   std::srand(std::time(0));

   // std::ofstream myfile;

   // size_t day = 0;
   std::cout << "Enter the population size: ";
   size_t population;
   std::vector<Person> populace;
   std::cin >> population;
   populace.resize(population);
   std::cout << "Enter how many days the simulation will run: ";
   size_t sim_run_time;
   std::cin >> sim_run_time;
   fill_population(populace, population);
   set_conn_nums(populace, population, 20);

   // for (Person individual : populace)
   // {
   //    std::cout << individual.get_max_conns() << " ";
   // }
   // std::cout << '\n';


   // print_per_vect(populace);
   // print_size_t_vec(curr_aggregate_status(populace));
   infect_people(populace);

   // print_size_t_vec(close_contacts(populace));

   // print_size_t_vec(curr_aggregate_status(populace));
   // spread_disease(populace, population, close_contacts(populace));
   // print_size_t_vec(curr_aggregate_status(populace));
   // spread_disease(populace, population, close_contacts(populace));
   // print_size_t_vec(curr_aggregate_status(populace));

   time_steps(populace, population, sim_run_time);


   // print_per_vect(populace);



   // std::cout << funk();

   myfile.close();

}
