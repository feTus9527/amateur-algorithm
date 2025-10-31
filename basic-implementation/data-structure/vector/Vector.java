import java.util.Arrays;
import java.util.Random;

public class Vector {

    private static final int EXPAND_RATIO = 2;

    private int count;

    private int size;

    private int[] data;

    public Vector(int n) {
        this.size = n;
        this.count = 0;
        this.data = new int[size];
    }

    public int insert(int pos, int n) {
        if (pos < 0 || pos > this.count) {
            return 0;
        }
        if (this.count == this.size) {
            this.expand();
        }
        for (int i = this.count; i > pos; i--) {
            this.data[i] = this.data[i - 1];
        }
        this.data[pos] = n;
        this.count += 1;
        return 1;
    }

    public int remove(int pos) {
        if (pos < 0 || pos >= this.count) {
            return 0;
        }
        for (int i = pos; i < this.count - 1; i++) {
            this.data[i] = this.data[i + 1];
        }
        for (int i = this.count - 1; i < this.size; i++) {
            this.data[i] = 0;
        }
        this.count -= 1;
        return 1;
    }

    private void expand() {
        int[] expanded = Arrays.copyOf(this.data, this.data.length * EXPAND_RATIO);
        this.data = expanded;
        this.size = expanded.length;
    }

    public String toString() {
        StringBuilder str = new StringBuilder();
        
        // 计算每个位置所需的最大宽度
        int[] widths = new int[this.data.length];
        for (int i = 0; i < this.data.length; i++) {
            int indexWidth = String.valueOf(i).length();
            int dataWidth = String.valueOf(this.data[i]).length();
            widths[i] = Math.max(indexWidth, dataWidth);
        }
        
        // 计算总宽度（包括数字之间的空格）
        int totalWidth = 0;
        for (int width : widths) {
            totalWidth += width;
        }
        // 加上数字之间空格的宽度
        totalWidth += (this.data.length - 1);
        
        // 顶部边框
        str.append("┌─");
        for (int i = 0; i < totalWidth; i++) {
            str.append("─");
        }
        str.append("─┐\n");
        
        // 索引行
        str.append("│ ");
        for (int i = 0; i < this.data.length; i++) {
            String format = "%" + widths[i] + "d";
            str.append(String.format(format, i));
            if (i < this.data.length - 1) {
                str.append(" "); // 添加数字间的空格
            }
        }
        str.append(" │\n");
        
        // 中间分隔线
        str.append("├─");
        for (int i = 0; i < totalWidth; i++) {
            str.append("─");
        }
        str.append("─┤\n");
        
        // 数据行
        str.append("│ ");
        for (int i = 0; i < this.data.length; i++) {
            String format = "%" + widths[i] + "d";
            str.append(String.format(format, this.data[i]));
            if (i < this.data.length - 1) {
                str.append(" "); // 添加数字间的空格
            }
        }
        str.append(" │\n");
        
        // 底部边框
        str.append("└─");
        for (int i = 0; i < totalWidth; i++) {
            str.append("─");
        }
        str.append("─┘\n");
        
        return str.toString();
    }

    public int getCount() {
        return this.count;
    }

    public int getSize() {
        return this.size;
    }

    public int[] getData() {
        return this.data;
    }

    public static void main(String[] args) {
        final int MAX_OPS = 20;
        final int VECTOR_LENGTH = 2;
        Random random = new Random();
        Vector vector = new Vector(VECTOR_LENGTH);

        for (int i = 0; i < MAX_OPS; i++) {
            int op = random.nextInt(4);
            int pos = random.nextInt(vector.getCount() + 2);
            if (op < 3) {
                int n = random.nextInt(10000);
                int result = vector.insert(pos, n);
                System.out.printf("insert %d at position %d from vector = %d\n", n, pos, result);
            } else {
                int result = vector.remove(pos);
                System.out.printf("remove at position %d from vector = %d\n", pos, result);
            }
            System.out.println(vector);
        }
    }
}
