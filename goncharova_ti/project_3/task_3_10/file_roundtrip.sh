#!/bin/bash
for i in {1..10}; do
  touch "test${i}.txt"
  echo "file test${i}.txt saved"
done

count=10

while [[ $count -gt 0 ]]; do
    rm "test${count}.txt"
    echo "file test${count}.txt deleted"
    ((count--))
done
