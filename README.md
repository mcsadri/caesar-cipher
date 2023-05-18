# caesar-cipher

### Author

- Manuch Sadri

### Overview

- An introduction to cryptography with the Caesar Cipher. Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

### Feature Tasks and Requirements

- [X] Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
  - [X] The phrase will then be `shifted` that many letters.
    - [X] E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
  - [X] Shifts that exceed 26 should wrap around.
    - [X]  E.g. encrypt(‘abc’,27) would return ‘bcd’.
- [X] shifts that push a letter out or range should wrap around.
  - [X] E.g. encrypt(‘zzz’,1) would return ‘aaa’.
- [X] Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
- [ ] Create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- [ ] Devise a method for the computer to determine if code was broken with minimal human guidance.

### Implementation Notes

- [ ] In order to accomplish a certain task you’ll need access to a corpus of English words.
  - [ ] A search on something like python list of english words should get you going.

### User Acceptance Testing

- [X] encrypt a string with a given `shift`
- [X] decrypt a previously encrypted string with the same `shift`.
- [X] encryption should handle upper and lower case letters.
- [X] encryption should allow non-alpha characters but ignore them, including white space.
- [ ] decrypt encrypted version of `It was the best of times, it was the worst of times.` WITHOUT knowing the shift used.
- [ ] refer to supplied [unit tests](./tests/test_cipher.py).