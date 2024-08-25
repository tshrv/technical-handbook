"use client";

import { useState, useEffect } from "react";
import { useSearchParams, useParams } from "next/navigation";
import { useRouter } from "next/navigation";
type Post = {
  id: number;
  userId: number;
  title: string;
  body: string;
};

export default function PostDetail() {
  const params = useParams<{ postId: string }>();
  const router = useRouter();
  const [data, setData] = useState<Post>();
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/posts/${params.postId}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("API Error");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setIsLoading(false);
      })
      .catch((error) => {
        setIsLoading(false);
        setError(error);
      });
  }, []);
  if (isLoading) return <p>Loading</p>;
  if (error) return <p>Error</p>;
  return (
    <div>
      <button
        onClick={() => {
          router.push("/post");
        }}
      >
        Back to Post List
      </button>
      <p>Post Detail</p>
      <p>#{params.postId}</p>
      <p>{data?.title}</p>
      <p>{data?.body}</p>
    </div>
  );
}
