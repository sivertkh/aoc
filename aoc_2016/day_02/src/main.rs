
fn run() -> () {
    let input = include_str!("input.txt").lines().map(|x| x.chars());

    let mut pos_x_1 = 1;
    let mut pos_y_1 = 1;
    let size_1 = 3;
    let mut res_1 = vec![];
    let kdb_1 = [["1","2","3"],["4","5","6"],["7","8","9"]];

    let kdb_2 = [
        ["", "", "1", "",""],
        ["", "2", "3", "4",""],
        ["5", "6", "7", "8","9"],
        ["", "A", "B", "C",""],
        ["", "", "D", "",""],
    ];
    let mut pos_x_2 = 2;
    let mut pos_y_2 = 0;
    let size_2 = 5;
    let mut res_2 = vec![];

    for line in input {
        for c in line {
            match c {
                'U' => {
                    if pos_x_1 > 0 {
                        pos_x_1 -= 1;
                    }
                    if pos_x_2 > 0 && kdb_2[pos_x_2-1][pos_y_2] != "" {
                        pos_x_2 -= 1;
                    }
                },
                'D' => {
                    if pos_x_1 < size_1 - 1 {
                        pos_x_1 += 1;
                    }
                    if pos_x_2 < size_2 - 1 && kdb_2[pos_x_2+1][pos_y_2] != "" {
                        pos_x_2 += 1;
                    }
                },
                'L' => {
                    if pos_y_1 > 0 {
                        pos_y_1 -= 1;
                    }
                    if pos_y_2 > 0 && kdb_2[pos_x_2][pos_y_2-1] != ""{
                        pos_y_2 -= 1;
                    }
                },
                'R' => {
                    if pos_y_1 < size_1 - 1 {
                        pos_y_1 += 1;
                    }
                    if pos_y_2 < size_2 - 1 && kdb_2[pos_x_2][pos_y_2+1] != ""{
                        pos_y_2 += 1;
                    }
                },
                _ => panic!(),
            }
        }
        res_1.push(kdb_1[pos_x_1][pos_y_1]);
        res_2.push(kdb_2[pos_x_2][pos_y_2]);
    }
    println!("Part 1: {}", res_1.join(""));
    println!("Part 2: {}", res_2.join(""));
}


fn main() {
    run();
}
