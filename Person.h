#ifndef PERSON_H
#define PERSON_H
#include <string>
#include <vector>
#include <iostream>


class Person
{
public:
   Person();
   Person(size_t index);
   std::string get_status_str() const;
   size_t get_max_conns();
   size_t get_status_num() const;
   size_t get_time_infected() const;
   void time_infected_plus();
   bool connections_full() const;
   size_t get_name() const;
   void infect();
   void heal();
   void kill();
   void set_health_state(size_t state);
   void set_max_connec(size_t num);

private:
   size_t _name;
   size_t _health_state;
   size_t _time_infected;
   size_t _max_connections;



};

#endif // PERSON_H
