class Solution
{
public:
    string toLowerCase(string s)
    {
        for (int i = 0; i < s.length(); i++)
        {
            int t = int(s[i]);
            if (t >= 65 && t <= 90)
            {
                t += 32;
                s[i] = char(t);
            }
        }
        return s;
    }
};