function setCookie(name, value) {
    const encodedValue = encodeURIComponent(value);
    const cookie = `${name}=${encodedValue};`;
    document.cookie = cookie;
}

setCookie('token', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkJsdWVUaWdlcjM0IiwicGFzcyI6ImNHRnpjeTUwZUhRSyIsImlhdCI6MTY5MzA5NDQwMH0.49imX4EZCIepFTJ9pHptOwH53b-7WhGSBHc_4LcAyTA');
