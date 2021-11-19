class Foo 
{

    private boolean printF;
    private boolean printS;
    
    public Foo() 
    {
        printF = false;
        printS = false;
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        if (!printF && !printS)
        {
            printFirst.run();
            printF = true;
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        while (!printF);
        if (printF && !printS)
        {
            printSecond.run();
            printS = true;
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        // printThird.run() outputs "third". Do not change or remove this line.
        while (!printF || !printS);
        if (printF && printS)
        {
            printThird.run();
            printF = false;
            printS = false;
        }
    }
}