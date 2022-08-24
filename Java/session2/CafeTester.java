public class CafeTester{
    public static void main(String[] args) {
        Cafe myCafe= new Cafe();
        myCafe.chaiLatte();
        myCafe.americano("Joe");
        myCafe.buildMenu();
        myCafe.customerList();
        myCafe.customerFavorites();
    }
    //Array
    //ArrayList using arrays inside this class
    
    //HashMap why use one? referring to data by keyname; storing multiple values in one dimension. HashMaps takes the information and puts it anywhere, it does not store things in sequences like an array or arrayList.  It is unordered, you access things by keys, there are no idx.
}