# Processing image for INGInious

Container image with processing language.

## Example of `run`
```bash
#!/bin/bash

getinput 1 > student/student.pde

raw_output=$(run_student processing-java --sketch=student --output=student/output --force --run 2> /dev/null)
output=$(echo $raw_output | sed -e 's/ Finished.//g') # Delete " Finished." from the output

if [ "$output" == "Hello, World!" ]; then
    feedback-result success
    feedback-msg -em "Your code is right! Output:\n\n"
else
    feedback-result failed
    feedback-msg -em "Your code is false. Output:\n\n"
fi

echo $output | feedback-msg -ae
```
