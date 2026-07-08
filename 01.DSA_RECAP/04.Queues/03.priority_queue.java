import java.util.PriorityQueue;

class Main {

    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.offer(30);
        pq.offer(80);
        pq.offer(40);
        pq.offer(20);

        System.out.println(pq);
    }
}
