#include "Person.h"

Person::Person(size_t index)
{
   _name = index;
   _health_state = 0;
   _max_connections = 3;
   // _num_connections = 0;
}

Person::Person(){}

size_t Person::get_max_conns()
{
   return _max_connections;
}

size_t Person::get_status_num() const
{
   return _health_state;
}

size_t Person::get_time_infected() const
{
   return _time_infected;
}

void Person::time_infected_plus()
{
   _time_infected++;
}

size_t Person::get_name() const
{
   return _name;
}

void Person::set_health_state(size_t state)
{
   _health_state = state;
}

// void set_max_connec

void Person::infect()
{
   set_health_state(1);
   _time_infected = 0;
}

void Person::heal()
{
   set_health_state(2);
}

void Person::kill()
{
   set_health_state(3);
}

/* returns whether a Person has run out of space to make connections
 */
// bool Person::connections_full() const
// {
//    if (_num_connections < _max_connections)
//    {
//       return false;
//    }
//    else
//    {
//       return true;
//    }
// }

std::string Person::get_status_str() const
{
   if (_health_state == 0)
   {
      return "this person is healthy";
   }
   else if (_health_state == 1)
   {
      return "this person is infected";
   }
   else if (_health_state == 2)
   {
      return "this person is recovered";
   }
   else //if(_health_state == 3)
   {
      return "this person died :((";
   }
}

void Person::set_max_connec(size_t num)
{
   _max_connections = num;
}
