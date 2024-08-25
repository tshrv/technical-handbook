"use client";

function calculate(numA: number, numB: number): number {
  return numA + numB;
}

const concat = (str1: string, str2: string = "default"): string => {
  return str1 + " " + str2;
};

function double(value: number): number;
function double(value: string): string;
function double(value: any): any {
  if (typeof value === "number") return value * 2;
  if (typeof value === "string") return value + value;
}

function addAllNumbers(...nums: number[]): number {
  return nums.reduce((prev, cur) => {
    return prev + cur;
  });
}

let numAndStr: (num: number, str: string) => string;
numAndStr = (num: number, str: string) => num + str;

let arr: number[] = [1, 2, 3, 4, 5, 6];
function sumOfSquaresOfEvenNumbers(nums: number[]): number {
  return nums
    .filter((value, idx, arr) => value % 2 == 0)
    .map((value, idx, arr) => value * value)
    .reduce((prev, cur) => prev + cur);
}
export default function Compute() {
  return (
    <div>
      <p>Compute</p>
      <p>{calculate(10, 12)}</p>
      <p>{concat("tushar")}</p>
      <p>{concat("sonali", "srivastava")}</p>
      <p>
        <b>Double</b>
      </p>
      <p>{double(10)}</p>
      <p>{double("10")}</p>

      <p>
        <b>Indefinite args</b>
      </p>
      <p>[1, 2, 3, 4, 5, 6]</p>
      <p>{addAllNumbers(1, 2, 3, 4, 5, 6)}</p>
      <p>numAndStr 10 + tushar = {numAndStr(10, "tushar")}</p>
      <p>
        sumOfSquaresOfEvenNumbers {arr} = {sumOfSquaresOfEvenNumbers(arr)}
      </p>
    </div>
  );
}
