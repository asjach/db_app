## PROPERTY
- box model



QFrame{
    color: #D9D9D9;
    background-color: #181818;
}


/* (dot) .QFrame  fix #141, #126, #123 */
.QFrame {
  border-radius: 4px;
  border: 1px solid #455364;
  /* No frame */
  /* HLine */
  /* HLine */
}

.QFrame[frameShape="0"] {
  border-radius: 4px;
  border: 1px transparent #455364;
}

.QFrame[frameShape="4"] {
  max-height: 2px;
  border: none;
  background-color: #455364;
}

.QFrame[frameShape="5"] {
  max-width: 2px;
  border: none;
  background-color: #455364;
}