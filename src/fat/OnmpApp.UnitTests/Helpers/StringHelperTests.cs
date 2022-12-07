namespace OnmpApp.UnitTests.Helpers;

public class StringHelperTests
{
    [Theory]
    [InlineData("")]
    [InlineData("adsads")]
    [InlineData("ads@akd@")]
    [InlineData("ads@dsa#a.ru")]
    // Тестирование неверного адреса почты
    public void IsEmail_False(string email)
    {
        Assert.False(email.IsEmail());
    }

    [Theory]
    [InlineData("a@m.ru")]
    [InlineData("a@m.ru.ru")]
    [InlineData("k.p.a@m.ru.ru")]
    [InlineData("LongMail@yandex.ru")]
    // Тестирование верного адреса почты
    public void IsEmail_True(string email)
    {
        Assert.True(email.IsEmail());
    }
}
