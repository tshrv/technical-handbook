import { useContext } from "react";
import { MyContext } from "@/lib/provider";

type SubHeadProps = {
  compute: (i: number, s: string) => number;
};
export default function SubHead({ compute }: SubHeadProps) {
  const { num, setNum } = useContext(MyContext);
  return (
    <div>
      <p>SubHead.num: {num}</p>
      <p>SubHead.Compute: {compute(100, "subhead.compute")}</p>
      <button onClick={() => setNum(num + 1)}>SubHead.increase</button>
    </div>
  );
}
