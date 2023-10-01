import java.util.Scanner;
class Primeno
{
	public static void main(String arg[])
	{
	int j,c;
               System.out.print("Enter n: ");
	Scanner s=new Scanner(System.in);
	int n=s.nextInt();
               System.out.println("Prime numbers: ");
	for(int i=2;i<=n;i++)
	{
	c=0;
	for(j=1;j<=i;j++)
	{
	   if(i%j==0)
	   {
	        c++;
	   }
	}
	if(c==2)
	       System.out.print(i+"  ");
	}
	}
}
