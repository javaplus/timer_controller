Timer controller is a python application that listens via REST API's for calls and broadcasts events to clients

Request messages expected to look something like the following:

```
{
   "minutes":"5",
   "speaktime":[
      {
         "time":"4:50",
         "say":"Make your plans ready.Make your plans ready"
      },
      {
         "time":"4:30",
         "say":"Test Fire, Test Fire, Test Fire"
      },
      {
         "time":"4:10",
         "say":"10,9, 8, 7, 6, 5, 4, 3, 2, 1"
      },
      {
         "time":"4",
         "say":"GO GO GO, GO GO GO, GO GO GO GO GO"
      },
      {
         "time":"3",
         "say":"3 minutes remaining, 3 minutes"
      },
      {
         "time":"2",
         "say":"2 minutes remaining, 2 minutes"
      },
      {
         "time":"1",
         "say":"1 minute remaining, 1 minute"
      },
      {
         "time":"0:10",
         "say":"10, 9, 8, 7, 6, 5, 4, 3, 2, 1, STOP, STOP, STOP, ,, STOP, STOP, STOP"
      }
   ],
   "speakinterval":[
      {
         "interval":"5",
         "say":"%min% Minutes Remaining, %min% Minutes."
      }
   ]
}

```

NOTE: The "speakinterval" is not currently used.
