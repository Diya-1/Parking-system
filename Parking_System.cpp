//parking system
#include<iostream>
#include<stdlib.h>
#define n 2
#define m 10
using namespace std;
int vehcount=0;
int carcount=0;
int bikecount=0;
void caradd(int car[n][m]){
    int num;
    cout<<"enter the number of car: ";
    cin>>num;
    int spy =0,full =0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(car[i][j]==0 && spy == 0){
                spy = 1;
            car[i][j] =num;
            carcount++;
            vehcount++;
            }
            else if(car[i][j]!=0){
                full++;
            }
        }
    }
    if(full == m*n)
    cout<<"No more slots are available for parking "<<endl;
    return ;
}
void bikeadd(int bike[n][m]){
    int num;
    cout<<"enter the number of bike: ";
    cin>>num;
    int spy =0,full=0;
    for(int i=0;i<n;i++){
        for(int j =0;j<m;j++){
            if(bike[i][j]==0 && spy ==0){
                spy =1;
            bike[i][j]=num;
            bikecount++;
            vehcount++;
            }
            else if(bike[i][j]!=0){
                full++;
            } 
        }
    }
    if(full == m*n){
        cout<<"No more slots are available for parking!"<<endl;
    }
    return ;
}
void display(int ar[n][m]){
    for (int i = 0; i < n; i++)
    {
        for(int j=0;j<m;j++){
            cout<<ar[i][j]<<"    ";
        }
        cout<<endl;
    }
       
}
void depart(int ar[n][m],int vnum){
    int flag =0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(ar[i][j]==vnum){
            ar[i][j]=0;
            flag =1;
            }
        }
    }
    if(flag == 0){
        cout<<"Not a parked vehicle number"<<endl;
    }
    return;
}
int main(){
    int car[n][m],choice;
    int bike[n][m],type;
    for(int i=0;i<2;i++){
        for(int j=0;j<10;j++){
            car[i][j]=0;
            bike[i][j]=0;
        }
    }
    // for(int i=0;i<2;i++){
    //     for(int j=0;j<20;j++){
    //         bike[i][j]=0;
    //     }
    // }
    do{
        system("CLS");
        cout<<"\nCar Parking\n";
        cout<<"1. Arrival of a vehicle\n";
        cout<<"2. Total no. of vehicles parked\n";
        cout<<"3. Total no. of cars parked\n";
        cout<<"4. Total no. of scooters parked\n";
        cout<<"5. Display order in which vehicles are parked\n";
        cout<<"6. Departure of vehicle\n";
        cout<<"7. Exit\n";
        cout<<"what you want ?"<<endl;
        cin>>choice;
        switch(choice){
        {
            case 1: system("CLS");
                    cout<<"enter [1] for car / [2] for bike"<<endl;
                    cin>>type;
                    if(type == 1)
                    caradd(car);
                    else if(type ==2)
                    bikeadd(bike);
                    else
                    cout<<"Invalid vehicle type";
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
            case 2:system("CLS");
                    cout<<"Total numbers of vehicle parked are: "<<vehcount;
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
            case 3:system("CLS");
                    cout<<"Total cars parked are : "<<carcount;
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
            case 4:system("CLS");
                    cout<<"Total bikes parked are : "<<bikecount;
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
            case 5:system("CLS");
                    cout<<"Slots of parking are: ";
                    cout<<"cars->"<<endl;
                    display(car);
                    cout<<"bikes->"<<endl;
                    display(bike);
                    system("pause");
                    cout<<"enter any key to continue";
                    getchar();
                    break;
            case 6: system("CLS");
                    int vnum;
                    cout<<"Departure"<<endl;
                    cout<<"enter vehicle type(1 for car / 2 for bike)";
                    cin>>type;
                    if(type == 1){
                    cout<<"enter vehicle number:";
                    cin>>vnum;
                    depart(car,vnum);}
                    else if(type == 2){
                        cout<<"enter vehicle number: ";
                        cin>>vnum;
                        depart(bike,vnum);
                    }
                    else 
                    cout<<"Invalid vehicle type";
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
            case 7: system("CLS");
                    cout<<"Thank You for using parking slots!!";
                    return -1;
            default :system("CLS");
                    cout<<"Invalid Choice";
                    system("pause");
                    cout<<"enter any key to continue: ";
                    getchar();
                    break;
        }
        }        
    }while(1);
    return 0;
}