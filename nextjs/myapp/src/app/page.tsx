"use client";

import {
  useState,
  useCallback,
  useMemo,
  useEffect,
  useContext,
  useRef,
} from "react";
import { useRouter } from "next/navigation";
import Head from "@/components/head";
import SubHead from "@/components/subhead";
import { MyContext } from "@/lib/provider";

export default function Home() {
  const router = useRouter();
  const [val, setVal] = useState<number>(0);
  const { num, setNum } = useContext(MyContext);
  useEffect(() => {
    console.log("Global Load");
    return () => console.log("Global Teardown");
  }, []);

  useEffect(() => {
    console.log("val effect in action");
    return () => console.log("val effect teardown");
  }, [val]);

  const compute = useCallback(
    (i: number, s: string) => {
      let resp = i + 1;
      console.log("compute", s, i, resp, num);
      return resp;
    },
    [num]
  );

  const memoizedComputedValue = useMemo(() => {
    console.log("computing memoizedComputedValue on", num);
    return compute(num, "usememo");
  }, [num]);

  const increment = () => {
    setVal(val + 1);
  };

  const decrement = () => {
    setVal(val - 1);
  };
  return (
    <div>
      Hello World
      <p>Count: {val}</p>
      <button className="border border-black p-2" onClick={() => increment()}>
        Increment
      </button>
      <button className="border border-black p-2" onClick={() => decrement()}>
        Decrement
      </button>
      <button onClick={() => router.push("/about")} className="text-blue-500">
        About
      </button>
      <button
        onClick={() => setNum(num + 1)}
        className="border border-black p-2"
      >
        Home.Num.Increase
      </button>
      <p>Home.Compute: {compute(num, "home.compute")}</p>
      <p>Home.memoizedComputedValue: {memoizedComputedValue}</p>
      <br />
      <Head compute={compute} />
      <br />
      <SubHead compute={compute} />
    </div>
  );
}
