# Prolog (SWI-Prolog) image for INGInious

Example of `run`:

```bash
#!/bin/bash

echo "#!/usr/bin/swipl -f -q" > student/test.pl
echo ":- initialization main." >> student/test.pl
getinput 1 >> student/test.pl
chmod +x student/test.pl

output=$(run_student ./student/test.pl 2> errors)
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
