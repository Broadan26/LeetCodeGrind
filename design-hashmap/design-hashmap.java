class MyHashMap {

    private Integer[] map;
    private final int size = 1000003;
    
    public MyHashMap() 
    {
        map = new Integer[size];
    }
    
    /*Hashes the given key to a key for the table*/
    private int hash(int key)
    {
        return key % size;
    }
    
    /*Inserts a (key, value) pair into the hashmap*/
    public void put(int key, int value) 
    {
        int newKey = hash(key);
        map[newKey] = value;
    }
    
    /*Returns the value which the specified key is mapped to*/
    public int get(int key) 
    {
        int newKey = hash(key);
        if (map[newKey] == null)
            return -1;
        return map[newKey];
    }
    
    /*Removes the key and its corresponding value from the map*/
    public void remove(int key) 
    {
        int newKey = hash(key);
        map[newKey] = null;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */