# Clojure image for INGInious

Example of `run`:
```bash
#!/bin/bash

getinput 1 > student/example.clj

output=$(run_student clojure student/example.clj 2> errors)
if [ "$( cat errors )" != "" ]; then
    feedback-result failed
    feedback-msg -em "There are errors in your code:\n\n"
    echo "$(cat errors)" | feedback-msg -ae
    exit
fi

if [ "$output" == "Hello, World!" ]; then
    feedback-result success
    feedback-msg -em "Your code is right! Output:\n\n"
else
    feedback-result failed
    feedback-msg -em "Your code is false. Output:\n\n"
fi

echo $output | feedback-msg -ae
```
