using System;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Saisir votre prenom : ");
        string prenom = Console.ReadLine();
        Console.WriteLine (string.Format("Hello {0}", prenom));
        Hello();
    }
    
    private static void Hello()
    {
        Console.WriteLine ("Saisir votre prenom : ");
        string prenom = Console.ReadLine();
        Console.WriteLine (string.Format("Hello {0}", prenom));
    }
}