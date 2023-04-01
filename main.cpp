#include <iostream>
#include<conio.h>
#include <windows.h>
#include <fstream>
using namespace std;

    char email[60],l_email[60],type[1];
    int l,l_l,t_l;


    // Email Type Finder and Length
    int check(char e[]){
    for(int i=0;e[i]!='@';i++){
        t_l=i;
    }

        type[0]=e[t_l+2];
    }

int main()
{
    int cnt=1,number_of_lines = 0,line;
    char choice[1],c[1];
    HANDLE hConsole;
    hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, 10);
    cout << "\t\t\t  Facebook Hidden_Email Bruter\n\t\t\t\t\tby Tig3r`Bh4i\n";
    SetConsoleTextAttribute(hConsole, 11);
    cout<<"\n\nFacebook Email: ";
    cin>>email;
    l=strlen(email);
    check(email);
    ifstream emails("emails.txt");
    if(!emails){
        SetConsoleTextAttribute(hConsole, 12);
        cout << "\aEmail List is Not Found !!!"<<endl;
        SetConsoleTextAttribute(hConsole, 14);
        cout << "I think the email list is not in the same directory \nOR\nMay Be File name is not 'emails.txt'";
        SetConsoleTextAttribute(hConsole, 11);
        cout<< "\nFor More Help contact @ \nwww.facebook.com/tiger6117\nwww.facebook.com/tigerzplac3";
    }

    while(!emails.eof()){

        emails>>l_email;
        l_l=strlen(l_email);
        if(l_l==l){

            if(l_email[t_l+2]==type[0]){

                if(l_email[0]==email[0] && l_email[t_l]==email[t_l])
                {
                    ofstream emails_found("Email_Found.txt", ios::app);
                    if(cnt==1){
                    SetConsoleTextAttribute(hConsole, 242);
                    cout<< "\nEmail-s Found !!!! \n";
                    SetConsoleTextAttribute(hConsole, 10);
                    cout<<l_email <<endl;
                    SetConsoleTextAttribute(hConsole, 10);
                    emails_found<< "\t\t Facebook Hidden_Email Bruter\n\t\t\t\tby Tig3r`Bh4i\n";
                    emails_found<< "\nEmail-s Found\n\nHidden Email:"<<email<<endl;
                    emails_found<< "\nBruted Email-s :" <<endl;
                    emails_found<<l_email <<endl;
                    cnt++;
                    }else{

                        SetConsoleTextAttribute(hConsole, 10);
                        cout<<l_email <<endl;
                        emails_found<<l_email <<endl;
                        cnt++;
                        emails_found.close();
                    }

                }
            }
        }
    }

    emails.close();
    if(cnt>1){
            SetConsoleTextAttribute(hConsole, 112);
            if(cnt==1){
                cout<<"\n\nTotal Email Found :";
                cout <<" "<<cnt-1;
            }else
        cout<<"\n\nTotal Emails Found :";
        SetConsoleTextAttribute(hConsole, 12);
        cout <<" "<<cnt-1;
        SetConsoleTextAttribute(hConsole, 10);
        cout<<"\nEmails Are Saved In Text File(Email_Found.txt)";
        SetConsoleTextAttribute(hConsole, 14);
        cout<<"\n\n\t\tFor More Tricky Stuff And Softwares \n";
        SetConsoleTextAttribute(hConsole, 15);
        cout<<"\n\n\t\t\tVisit:";
        SetConsoleTextAttribute(hConsole, 10);
        cout<<"\n\t\twww.tigerzplace.tk\n\t\t\twww.softwarezcity.ml\n";
        SetConsoleTextAttribute(hConsole, 11);
        cout<<"\n\t\twww.facebook.com/tigerzplac3";
    }else{
        SetConsoleTextAttribute(hConsole, 12);
        cout<< "\n\n\t\a): Sorry !!! No Emails Are Found In The list :(";
        SetConsoleTextAttribute(hConsole, 14);
        cout<<"\n\t  For More Tricky Stuff And Softwares \n";
        SetConsoleTextAttribute(hConsole, 15);
        cout<<"\n\n\t\t\tVisit:";
        SetConsoleTextAttribute(hConsole, 10);
        cout<<"\n\t\twww.tigerzplace.tk\n\t\t\twww.softwarezcity.ml\n";
         SetConsoleTextAttribute(hConsole, 11);
        cout<<"\n\t\twww.facebook.com/tigerzplac3";
    }
    getch();
}
