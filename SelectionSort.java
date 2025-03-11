class SelectionSort{
    public static void main(String[] args){
	int[] test_arr = [5,4,3,2,1];
	selectionSort(test_arr);
	for(int i : test_arr){
		System.out.print(i + " ");
	}
}
    
    public static void selectionSort(int[] arr){
        int n = arr.length;
        for(int i = 0; i < n-1; i++){
            int min = i;
            for(int j = i+1; j < n; j++){
                if(arr[j] < arr[min]){
                    min = j;
                }
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }

}
