using System.Text.RegularExpressions;

namespace OnmpApp.Helpers;

public static class StringHelper
{
    public static bool IsEmail(this string str)
    {
        if (string.IsNullOrEmpty(str))
            return false;
        string pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$";
        return Regex.IsMatch(str.ToLower(), pattern);
    }
}
