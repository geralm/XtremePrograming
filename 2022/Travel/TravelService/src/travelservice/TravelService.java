/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package travelservice;
import java.util.*;
import java.lang.*;
import java.io.*;
/**
 *
 * @author Esteb
 */


    /**
     * @param args the command line arguments
     */


// Please name your class Main
class Main {
    public static void main (String[] args) throws java.lang.Exception {
//        Scanner in = new Scanner(System.in);
//            int a = in.nextInt();
//            int stations = in.nextInt();
//            int start_fuel = in.nextInt();
//            int start_cost = in.nextInt();
//
//            for(int i = 0; i <a; i++){
//                Structure s = new Structure(stations, start_fuel, start_cost);
//                for(int j = 0; j<stations; j++){
//                    int b = in.nextInt();
//                    if(j % 2 == 0){
//                        s.addStation(b);
//                    }else{
//                        s.setWeight(b);
//                    }
//                }
//                System.out.println(s.cost());
//
//
//
//
//            }
        
        Structure s = new Structure(3, 35, 230);
        s.addStation(15 , 240 );
        s.addStation(18,225);
        s.addStation(24,240);
        System.out.println(s.cost());


    }
    public static class Structure {
        int nodes; 
        ArrayList<Integer> list; 
        ArrayList<Integer> weights; 
        int start_fuel;
        int start_cost;
        public Structure(int nodes, int start_fuel, int start_cost) {

           this.nodes = nodes;
           this.start_fuel = start_fuel;
           this.start_cost = start_cost;
            list = new ArrayList<>(); 
            weights = new ArrayList<>() ; 
        }
        public int cost(){
            return getMinimunCost(start_fuel*start_cost,start_fuel , start_cost);
        }
        public void addWeight( int b){
            weights.add(b);
        }

        public void addStation(int weight, int station){
            list.add(station);   
            weights.add(weight);
        }
        private void goNext(){
            list.remove(0);
            weights.remove(0);
        }
        private int goTo(int init, int dest){
            for(int i = init; i<dest; i++){
                this.start_fuel-= list.get(i);
                goNext();
            }
            return (weights.get(0)*list.get(0))+500;
        }
        private int cheapest(int a, int min){
            if(a ==0){
                return min;
            }else{
                if(min < list.get(a)){
                    return cheapest(a-1, min);
                }else{
                     return cheapest(a-1, list.get(a));
                }
            }
        }
        private int getCurrent( ){
            return this.list.get(0);
        }
        public int search(int entry){

            for(int i = 0; i<this.list.size(); i++){
                if (entry == this.list.get(i)){
                    return i;
                }
            }
            return 0;
        }


        private int getMinimunCost(int sum, int gas, int rate){
            if(this.list.isEmpty()){
                return sum;
            }else{
                int ms = getMinimunScope(gas, this.list.size()-1);
                int c = cheapest(ms,9999999 );
                int s = search(c);
                int a = goTo(s);
                return getMinimunCost(sum+a, gas, rate);
            }
        }
        private int getMinimunScope(int gas, int i){
            if(getScope(0, 0, i) <= gas){
                return i;
            }else{
                return getMinimunScope(gas, i-1);
            }
        }

        private int getScope(int sum,int a, int b){
            if(a==b){
                return sum;
            }
            else {
                return getScope(sum+ weights.get(a), a+1, b);
            }
        }




    }
}
 
    


