import { MyContext } from "@/lib/provider";
import { useContext } from "react";

type HomeProps = {
  compute: (i: number, s: string) => number;
};
export default function Head({ compute }: HomeProps) {
  const { num, setNum } = useContext(MyContext);
  return (
    <div>
      <p>Head.num: {num}</p>
      <p>Head.compute: {compute(100, "head.compute")}</p>
      <button onClick={() => setNum(num + 1)}>Head.increase</button>
    </div>
  );
}
