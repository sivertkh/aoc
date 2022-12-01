use std::{fs, path::Path};

fn read_file(filename: impl AsRef<Path>) -> Result<Vec<u32>, Box<dyn std::error::Error>> {
    let mut data: Vec<u32> = fs::read_to_string(filename)?
        .split("\n\n")
        .map(|x| {
            x.split_terminator("\n")
                .map(|s| s.parse::<u32>().unwrap())
                .sum()
        })
        .collect();
    data.sort();
    Ok(data)
}

fn main() {
    let data = read_file("day_01/input.txt");

    match data {
        Ok(input_data) => {
            println!("Part 1: {}", input_data.last().unwrap());
            println!(
                "Part 2: {}",
                input_data.as_slice()[input_data.len() - 3..]
                    .iter()
                    .sum::<u32>()
            );
        }
        Err(err) => {
            println!("{:?}", err);
        }
    }
}
