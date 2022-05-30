#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int get_nr_of_lines(FILE *fp)
{
    char ch;
    int line_nr = 0;
    while (!feof(fp))
    {
        ch = fgetc(fp);
        if (ch == '\n')
        {
            line_nr++;
        }
    }
    return line_nr;
}

int read_input(FILE *fp, int data[])
{
    int cur_mass = 0;
    int i = 0;
    while (fscanf(fp, "%d", &cur_mass) == 1)
    {
        data[i++] = cur_mass;
    }
    return 1;
}

int part_1(int data[], size_t s)
{
    int result = 0;
    for (int i = 0; i < s; i++)
    {
        result += (data[i] / 3) - 2;
    }
    return result;
}

int array_sum(int data[], size_t s)
{
    int sum = 0;
    for (int i = 0; i < s; i++)
    {
        if (data[i] > 0)
        {
            sum += data[i];
        }
    }
    return sum;
}

int part_2(int data[], size_t s)
{
    int fuel_req = 0;
    int fuel[s];
    for (int i = 0; i < s; i++)
    {
        fuel[i] = data[i];
    }
    bool change = true;
    int iteration = 0;

    while (change)
    {
        change = false;
        for (int i = 0; i < s; i++)
        {
            if (fuel[i] > 0)
            {
                int tmp = (fuel[i] / 3) - 2;
                if (tmp > 0)
                {
                    fuel[i] = tmp;
                    change = true;
                }
                else
                {
                    fuel[i] = 0;
                }
            }
        }
        fuel_req += array_sum(fuel, s);
    }
    return fuel_req;
}

int main(int argc, char const *argv[])
{
    FILE *fp;
    char ch;
    fp = fopen("input.txt", "r");
    if (fp == NULL)
    {
        exit(1);
    }
    int line_nr = get_nr_of_lines(fp);
    int data[line_nr];
    rewind(fp);
    read_input(fp, data);
    fclose(fp);

    printf("Part 1: %d \n", part_1(data, line_nr));
    printf("Part 2: %d \n", part_2(data, line_nr));
    return 0;
}
