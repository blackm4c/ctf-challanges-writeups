# Pretty HTML Page

## Concept

Based on PHP bug as discovered in CVE-2024-21726. Participants are supposed to exploit the inconsistent behaviour of PHP's multibyte string methods.

## Writeup

The comparison of the input string and `"flag"` is done with PHP's `mb_strpos` and `mb_substr`. Up to PHP 8.2, those methods count characters in a string differently as soon as there are broken UTF-8 characters present [1]. Since this challenge is using PHP 8.2, this bug can be exploited by sending a string containing `"flag"`, prepended by just enough bytes that form invalid UTF-8 characters (see [this script](solver.py) for an exploit).

There is also a comprehensive blog post further explaining the bug in context of the CVE mentioned above [2].

## References

[1] [GitHub PR fixing bug](https://github.com/php/php-src/pull/12913)  
[2] [Sonar on CVE-2024-21726](https://www.sonarsource.com/blog/joomla-multiple-xss-vulnerabilities/)
