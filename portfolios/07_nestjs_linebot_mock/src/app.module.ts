import { Module } from '@nestjs/common';
import { WebhookController } from './webhook.controller';
import { NotifyService } from './notify.service';

@Module({
  controllers: [WebhookController],
  providers: [NotifyService],
})
export class AppModule {}
