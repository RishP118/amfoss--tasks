use std::io;

fn prime(j: i32) -> bool {
    if j<=1 {
        return false; 
    }
    for i in 2..j {
        if j%i == 0 {
            return false;
        }
    }
    true 
}

fn main() {
    println!("Enter n:");
    
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("Error");

    let n: i32 = match n.trim().parse() {
        Ok(j) => j,
        Err(_) => {
            println!("Error");
            return;
        }
    };

    for i in 1..=n {
        if prime(i) {
            println!("{}", i);
        }
    }
}

