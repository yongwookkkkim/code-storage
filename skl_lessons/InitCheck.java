class InitCheck{
    public int instVal=1;
    public static int staVal=1;

    public InitCheck(){
        instVal++;
        staVal++;
    }

    {
        instVal++;
        staVal++;
    }

    static{
        staVal++;
    }
}
