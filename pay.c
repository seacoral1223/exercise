#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define MAX_MAILBOX 3

typedef struct {
    int data[MAX_MAILBOX];
    int count;
} Mailbox;

// 模拟发送选项
typedef enum {
    WAIT_FOREVER,
    WAIT_TIMEOUT,
    NO_WAIT,
    BUFFER_MSG
} SendOption;

// 模拟邮箱
Mailbox box = {.count = 0};

// 模拟接收（释放空间）
void receive_msg() {
    if (box.count > 0) {
        printf("接收消息: %d\n", box.data[0]);
        for (int i = 1; i < box.count; i++) {
            box.data[i - 1] = box.data[i];
        }
        box.count--;
    }
}

// 模拟发送
int mach_msg_sim(int msg, SendOption option, int timeout_ms) {
    clock_t start = clock();

    while (1) {
        if (box.count < MAX_MAILBOX) {
            box.data[box.count++] = msg;
            printf("发送成功: %d\n", msg);
            return 0;
        }

        // 邮箱满
        switch (option) {
            case WAIT_FOREVER:
                printf("邮箱满，等待中...\n");
                sleep(1);
                break;

            case WAIT_TIMEOUT:
                if ((clock() - start) * 1000 / CLOCKS_PER_SEC > timeout_ms) {
                    printf("超时，发送失败\n");
                    return -1;
                }
                printf("等待中(带超时)...\n");
                usleep(200000);
                break;

            case NO_WAIT:
                printf("邮箱满，立即返回失败\n");
                return -1;

            case BUFFER_MSG:
                printf("邮箱满，缓存消息: %d\n", msg);
                return 1;
        }
    }
}

// 主函数测试
int main() {
    // 填满邮箱
    mach_msg_sim(1, WAIT_FOREVER, 0);
    mach_msg_sim(2, WAIT_FOREVER, 0);
    mach_msg_sim(3, WAIT_FOREVER, 0);

    printf("\n=== 测试 NO_WAIT ===\n");
    mach_msg_sim(4, NO_WAIT, 0);

    printf("\n=== 测试 WAIT_TIMEOUT ===\n");
    mach_msg_sim(5, WAIT_TIMEOUT, 1000);

    printf("\n=== 测试 BUFFER_MSG ===\n");
    mach_msg_sim(6, BUFFER_MSG, 0);

    printf("\n=== 释放一个消息 ===\n");
    receive_msg();

    printf("\n=== 再发送 ===\n");
    mach_msg_sim(7, WAIT_FOREVER, 0);

    return 0;
}