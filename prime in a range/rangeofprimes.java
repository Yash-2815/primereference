import java.util.*;
import java.lang.*;
public class rangeofprimes {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int l=sc.nextInt(),r=sc.nextInt();
        int[] primes=new int[r+1];
        int count=0;
        primes[0]=0;
        primes[1]=0;
        for(int i=2;i<=r;i++){
            primes[i]=1;
        }
        for(int i=2;i*i<=r;i++){
            if(primes[i]==1){
                for(int j=i*i;j<=r;j+=i){
                    primes[j]=0;
                }
            }
        }
        for(int i=0;i<=r;i++){
            count+=primes[i];        //prefix sum calculation to know how many primes upto a given number
            primes[i]=count;         //EX:to calculate to how many primes are there upto 15.then ans=primes[15] ==>6
        }
        for(int i:primes){
            System.out.print(i+" ");
        }
        System.out.println();
        System.out.printf("The number of primes in between l and r:%d",(primes[r]-primes[l-1]));

    }
}
