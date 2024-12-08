/**
 * AOC 2024
 * --- Day 7: Bridge Repair ---
 */

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

struct targetSum
{
    long target;
    int numbers[20];
    int nr_of_numbers;
};

unsigned long nr_of_sums(FILE *fp)
{
    if (fp == NULL)
        exit(EXIT_FAILURE);

    char str[100];
    unsigned long linecount = 0;
    while (fgets(str, 100, fp) != NULL)
        linecount++;

    fseek(fp, 0, SEEK_SET);
    return linecount;
}

struct targetSum *parse_file(FILE *fp, unsigned long nr)
{
    char str[100];
    struct targetSum *ts = malloc(sizeof(struct targetSum) * nr);
    int i = 0;

    while (fgets(str, 100, fp) != NULL)
    {
        char *token = strtok(str, ":");
        ts[i].target = atol(token);

        token = strtok(strtok(NULL, ":"), " ");
        int number_count = 0;
        while (token != NULL)
        {
            ts[i].numbers[number_count] = atoi(token);
            number_count += 1;
            token = strtok(NULL, " ");
        }
        ts[i].nr_of_numbers = number_count;
        i++;
    }
    return ts;
}

int sum_part_1(long target, long cur_sum, int *numbers, int cur_num, int max_num)
{

    if (cur_num == max_num)
    {
        if (target == cur_sum)
            return 1;
        else
            return 0;
    }

    if (sum_part_1(target, cur_sum * numbers[cur_num], numbers, cur_num + 1, max_num))
        return 1;
    if (sum_part_1(target, cur_sum + numbers[cur_num], numbers, cur_num + 1, max_num))
        return 1;
    return 0;
}

int sum_part_2(long target, long cur_sum, int *numbers, int cur_num, int max_num)
{

    if (cur_num == max_num)
    {
        if (target == cur_sum)
            return 1;
        else
            return 0;
    }

    char tmp[256];
    sprintf(tmp, "%ld%d", cur_sum, numbers[cur_num]);

    if (sum_part_2(target, atol(tmp), numbers, cur_num + 1, max_num))
        return 1;

    if (sum_part_2(target, cur_sum * numbers[cur_num], numbers, cur_num + 1, max_num))
        return 1;

    if (sum_part_2(target, cur_sum + numbers[cur_num], numbers, cur_num + 1, max_num))
        return 1;

    return 0;
}

int main()
{
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    unsigned long nr = nr_of_sums(fp);
    struct targetSum *ts = parse_file(fp, nr);
    fclose(fp);

    long p1 = 0;
    long p2 = 0;

    for (unsigned long k = 0; k < nr; k++)
    {
        if (sum_part_1(ts[k].target, ts[k].numbers[0], ts[k].numbers, 1, ts[k].nr_of_numbers))
            p1 += ts[k].target;
        else if (sum_part_2(ts[k].target, ts[k].numbers[0], ts[k].numbers, 1, ts[k].nr_of_numbers))
            p2 += ts[k].target;
    }

    // free(ts);

    printf("Part 1: %ld\n", p1);
    printf("Part 2: %ld\n", p1 + p2);
    return EXIT_SUCCESS;
}
