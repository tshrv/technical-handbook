"use client";

import { useEffect } from "react";

interface Person {
  // readonly name: string;
  name: string;
  age?: number;
  greet(): string;
}

const p: Person = {
  name: "Tushar",
  age: 22,
  greet(): string {
    return `${this.name} says Hi`;
  },
};
console.log(p);
p.name = "Sonali";
console.log(p.greet());

interface Add {
  (a: number, b: number): number;
}
const add: Add = (x: number, y: number) => x + y;
console.log(add(1, 20));

class Animal {
  // private name: string;
  // protected name: string;
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  makeSound(): string {
    return `${this.name} makes sound`;
  }
  getName(): string {
    return this.name;
  }
}

let shero = new Animal("shero");
console.log("shero.name", shero.name);
console.log("shero.getName()", shero.getName());
console.log("shero.makeSound()", shero.makeSound());

class Dog extends Animal {
  makeSound(): string {
    return `${this.name} is a dog and it barks`;
  }
}
let sam = new Dog("Sam");
console.log("sam.makeSound()", sam.makeSound());

// Interface
interface Vehicle {
  brand: string;
  drive(): string;
}

class Car implements Vehicle {
  brand: string;
  constructor(brand: string) {
    this.brand = brand;
  }
  drive(): string {
    return `${this.brand} is moving`;
  }
}

let car = new Car("Hyundai");
console.log("car.brand", car.brand);
console.log("car.drive", car.drive());

//  abstract class

abstract class AbstractUser {
  abstract username: string;
  constructor() {}
  abstract getUsername(): string;
}

class User extends AbstractUser {
  username: string;
  constructor(username: string) {
    super();
    this.username = username;
  }
  getUsername(): string {
    return this.username;
  }
}

// let usr = new AbstractUser("tshrv");
let usr = new User("tshrv");
console.log("usr.getUsername", usr.getUsername());

// types
type ID = number | string;
let userId: ID;
userId = 1;

type TAddress = {
  city: string;
  state: string;
};

type TPerson = {
  name: string;
  address: TAddress;
};

let p1: TPerson = {
  name: "Tushar",
  address: {
    city: "Lucknow",
    state: "UP",
  },
};

console.log("p1", p1);

type Status = "pending" | "success" | "failed";
const status: Status = "pending";

// Intersection
type TEmail = {
  email: string;
  // name: number; // type never
};
type Employee = TPerson & TEmail;
let emp: Employee = {
  name: "Tushar",
  address: {
    city: "Lko",
    state: "UP",
  },
  email: "tshrv@gmail.com",
};

// funtion type
type MathOp = (a: number, b: number) => number;
const addOp: MathOp = (a, b) => a + b;

// Pick and Omit

type TPerson1 = {
  name: string;
  age: number;
  email: string;
  address: string;
  mobile: string;
};
type TContactInfo = Pick<TPerson1, "name" | "email" | "address" | "mobile">;
type TMailingInfo = Omit<TContactInfo, "email" | "name">;
//  Enums
enum Direction {
  up = -100,
  down,
  left,
  right,
}
console.log("Direction.up", Direction.up);
console.log("Direction.down", Direction.down);
console.log("Direction.left", Direction.left);
console.log("Direction.right", Direction.right);
console.log("Direction", Direction);
console.log("Direction[0]", Direction[0]);
console.log("Direction[1]", Direction[1]);
console.log("Direction[2]", Direction[2]);
console.log("Direction[3]", Direction[3]);

enum RespStatus {
  Success = "SUCCESS",
  Failure = "FAILURE",
  Pending = "PENDING",
  Other = 0,
}
console.log("RespStatus", RespStatus);
console.log("RespStatus.Success", RespStatus.Success);
console.log("RespStatus.Failure", RespStatus.Failure);
console.log("RespStatus.Pending", RespStatus.Pending);
console.log("RespStatus.Other", RespStatus.Other);

enum TrafficLight {
  Red,
  Green,
  Orange,
  Other,
}

function getAction(light: TrafficLight) {
  switch (light) {
    case TrafficLight.Red:
      return "Stop";
    case TrafficLight.Orange:
      return "Wait";
    case TrafficLight.Green:
      return "Go";
    default:
      return "Invalid";
  }
}
console.log(getAction(TrafficLight.Other));

// Generics
function genFunc<T>(arg: T): T {
  return arg;
}
genFunc<string>();
genFunc<boolean>();

interface GenIface<T> {
  val: T;
  time: Date;
  fn(arg: T): T;
}
const ob: GenIface<string> = {
  val: "Value",
  time: new Date(),
  fn(arg: string): string {
    return arg + "1";
  },
};

class Data<T> {
  value: T;
  constructor(value: T) {
    this.value = value;
  }
  getValue(): T {
    return this.value;
  }
}

let d1 = new Data<string>("String data");
d1.getValue();

let d2 = new Data<number>(12);
d2.getValue();

interface Lengthwise {
  length: number;
}

function logLength<T extends Lengthwise>(arg: T): void {
  console.log(arg.length);
}

logLength<string>("Tushar");
// logLength<number>(10);
logLength<number[]>([1, 2, 3, 4]);

// merge types
function merge<Z, K>(ob1: Z, ob2: K): Z & K {
  return { ...ob1, ...ob2 };
}

console.log(
  merge<{ name: string }, { age: number }>({ name: "Tushar" }, { age: 12 })
);

// default generic
function wrap<T = string>(val: T): T[] {
  return [val];
}
console.log(wrap<number>(10));

// Component
export default function Oop() {
  return (
    <div>
      <p>OOP</p>
    </div>
  );
}
