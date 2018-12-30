use std::collections::HashSet;
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;


#[derive(Debug)]
struct Inst {
    op_code: String,
    a: usize,
    b: usize,
    c: usize,
}

fn run_program(program: &Vec<Inst>, ip_reg: usize) {
    let mut ip: usize = 0;
    let mut register = [0; 6];

    let mut halt_values  = HashSet::<usize>::new();
    let mut last: usize = 0;
    loop {
        let cur = &program[ip];

        if ip == 28 {

            if halt_values.is_empty() {
                println!("Part1: {}", &register[4]);
            }
            if halt_values.contains(&register[4]) {
                println!("Part2: {}", last);
                break;
            }
            halt_values.insert(register[4]);
            last = register[4];
        }

        match cur.op_code.as_str() {
            "addr" => {register[cur.c] = register[cur.a] + register[cur.b]},
            "addi" => {register[cur.c] = register[cur.a] + cur.b},
            "mulr" => {register[cur.c] = register[cur.a] * register[cur.b]},
            "muli" => {register[cur.c] = register[cur.a] * cur.b},
            "banr" => {register[cur.c] = register[cur.a] & register[cur.b]},
            "bani" => {register[cur.c] = register[cur.a] & cur.b},
            "borr" => {register[cur.c] = register[cur.a] | register[cur.b]},
            "bori" => {register[cur.c] = register[cur.a] | cur.b},
            "setr" => {register[cur.c] = register[cur.a]},
            "seti" => {register[cur.c] = cur.a},
            "gtir" => {register[cur.c] = if cur.a > register[cur.b] {1} else {0}},
            "gtri" => {register[cur.c] = if register[cur.a] > cur.b {1} else {0}},
            "gtrr" => {register[cur.c] = if register[cur.a] > register[cur.b] {1} else {0}},
            "eqir" => {register[cur.c] = if cur.a == register[cur.b] {1} else {0}},
            "eqri" => {register[cur.c] = if register[cur.a] == cur.b {1} else {0}},
            "eqrr" => {register[cur.c] = if register[cur.a] == register[cur.b] {1} else {0}},
            _ => panic!("Unknown operator code!"),
        }
        
        if register[ip_reg] != ip {
            // Jump!
            ip = register[ip_reg];
        }
        // Move the ip
        ip += 1;
        register[ip_reg] = ip;
    }
}

fn run() -> () {
    let mut input = include_str!("input.txt").lines();
    let ip_register: usize = input.next().unwrap().trim_start_matches("#ip ").parse().unwrap();
    let mut program: Vec<Inst> = vec![];

    for i in input {
        let mut tmp: Vec<&str> = i.split(" ").collect();
        println!("{:?}", tmp);
        program.push(Inst{op_code: tmp[0].to_string(), 
                          a: tmp[1].to_string().parse::<usize>().unwrap(), 
                          b: tmp[2].to_string().parse::<usize>().unwrap(), 
                          c: tmp[3].to_string().parse::<usize>().unwrap()
                         }
        );
    }
    run_program(&program, ip_register);
}

fn main() {

    run();
}

