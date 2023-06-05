namespace OnmpApp.Helpers;

public static class UriHelper
{
    // Комбинирование нескольких путей адреса
    public static string CombineUri(params string[] uriParts)
    {
        string uri = string.Empty;
        if (uriParts != null && uriParts.Length > 0)
        {
            char[] trims = new char[] { '\\', '/' };
            uri = (uriParts[0] ?? string.Empty).TrimEnd(trims);
            for (int i = 1; i < uriParts.Length; i++)
            {
                uri = $"{uri.TrimEnd(trims)}/{(uriParts[i] ?? string.Empty).TrimStart(trims)}";
            }
        }
        return uri;
    }
}
