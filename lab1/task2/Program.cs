﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace task2
{
    class Student
    {
        public string Name;                              //ставим данные
        public string ID;
        public int year;

        public Student (string Name, string ID)    //констрактор с двумя параметрами для доступа на данных
        {
            this.Name= Name;
            this.ID=ID;
        }

        public void addYear()         //прибавляем год
        {
            year++;
        }
    }
     
    class Program
    {
      static void Main(string[] args)
      {
            Student s = new Student("Narkyz", "18BD113310");               //вводим данные призывая функцию
            s.year =1;
            s.addYear();                                                     //призываем увеличитель

            Console.Write(s.Name + " " + s.ID + " " + s.year);           //выводим на консоль
            Console.ReadKey();
      }
    }         

}
