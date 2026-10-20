// // in c 8types of opretors
// arithametic
// assignment
// logical 
// relational 
// increment/decrement
// conditionol
// special
// bitwise

// ===========ARITHEMETIC OPRETOR============
// + ,- ,/,*

//==========RELATIONAL OPRETORS=========
// it is show relation between two opreands
// compare two oprends
// in c language a non zero value are true.
// == ,>,>=,<,<=,!= 
// it have not true and false is like 3>4 is false ,7>2 true but in c not give t/f.
// it is give 1,0 (1 when true ,0 when false)

// ============logical opretors=========
// logics btwn  some conditon 
// AND ,OR ,NOT
// &&  ,||,!
// AND (&&)
// #include<stdio.h>
// #include<math.h>
// int main(){
//     printf("%d",4>3 && 5>2);
//     return 0;
// }
// in this case ans true mean output is 1 bcz both condtion are true
// #include<stdio.h>
// #include<math.h>
// int main(){
//     printf("%d",4<3 && 5>2);
//     return 0;
// }
// output is false mean 0 bcz one true and second is false
// #include<stdio.h>
// #include<math.h>
// int main(){
//     printf("%d",4<3 && 5<2);
    // return 0;
// }
// output is 0 bcz both are false

// OR (||)
// when we have multiple statment and there btwn OR opretor and anyone statement is true so anser is true 0

// #include<stdio.h>
// #include<math.h>
// int main(){
//     printf("%d",4>3 || 5<2 || 6>9 || 3>8 || 4>9);
//     return 0;
// }

// NOT (!)
// NOT is reverse output 
// #include<stdio.h>
// #include<math.h>
// int main(){
//     printf("%d",!(4>3) );
//     return 0;
// }
// ===================ASSIGNMENT OPRETOR===============
// assignment opretors assign the value it is also called short hand opretors
// = ,+=,-=,*=,/=,%=
// #include<stdio.h>
// int main(){
//     int a = 7;
//     int b = 3;
//     int c = 2;
//     int d = a+b;
//     printf("the value of d  is %d \n",d);
//     c +=d;
//     printf("the total is %d",c);
//     return 0;
// } 
// we have on more most impoertant opretor .
// TERNERY OPRETOR
// =====================TERNERY OPRETOR==================
// #include<stdio.h>
// int main(){
//     int a;
//     int b;
//     printf("Enter a:");
//     scanf("%d",&a);
//     printf("Enter b:");
//     scanf("%d",&b);
//     a>b?printf("a is greater....."):printf("b is greater....");
//     return 0;
// }